import random
from flask import Flask, jsonify, request, session

app = Flask(__name__, template_folder='.')
app.secret_key = 'ibm_casino_quantum_core_key_2026'

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

USERS_DB = {
    'itai': {'password': '123', 'balance': 10000, 'role': 'admin'},
    'guest': {'password': '123', 'balance': 1000, 'role': 'user'}
}

def get_card_value(card, current_score):
    rank = card['rank']
    if rank == '?': return 0
    if rank in ['J', 'Q', 'K']: return 10
    if rank == 'A': return 11 if current_score + 11 <= 21 else 1
    return int(rank)

def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        if card['rank'] == '?': continue
        if card['rank'] == 'A': aces += 1
        else: score += get_card_value(card, score)
    for _ in range(aces):
        score += 11 if score + 11 <= 21 else 1
    return score

@app.route('/')
def index():
    if 'username' not in session:
        session['username'] = 'guest'
        session['role'] = 'user'
    return open('index.html', 'r', encoding='utf-8').read()

@app.route('/api/auth/register', methods=['POST'])
def auth_register():
    data = request.get_json(force=True)
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()
    
    if not username or not password:
        return jsonify({'error': 'Username and password fields are required.'}), 400
    if username in USERS_DB:
        return jsonify({'error': 'This identity already exists in the registry.'}), 400
        
    USERS_DB[username] = {'password': password, 'balance': 1000, 'role': 'user'}
    return jsonify({'success': True, 'msg': 'Identity successfully registered.'})

@app.route('/api/auth/login', methods=['POST'])
def auth_login():
    data = request.get_json(force=True)
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()
    
    if username in USERS_DB and USERS_DB[username]['password'] == password:
        session['username'] = username
        session['role'] = USERS_DB[username]['role']
        return jsonify({'success': True, 'username': username, 'role': session['role'], 'balance': USERS_DB[username]['balance']})
    return jsonify({'error': 'Access denied. Invalid credentials.'}), 401

@app.route('/api/auth/status', methods=['GET'])
def auth_status():
    username = session.get('username', 'guest')
    role = session.get('role', 'user')
    balance = USERS_DB[username]['balance'] if username in USERS_DB else 1000
    return jsonify({'username': username, 'role': role, 'balance': balance, 'all_users': list(USERS_DB.keys())})

@app.route('/api/admin/deposit', methods=['POST'])
def admin_deposit():
    if session.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized system access.'}), 403
    
    data = request.get_json(force=True)
    target_user = data.get('username', '').lower()
    amount = int(data.get('amount', 0))
    
    if target_user in USERS_DB:
        USERS_DB[target_user]['balance'] += amount
        return jsonify({'success': True, 'msg': f'Injected ${amount} into {target_user}\'s vault.'})
    return jsonify({'error': 'Target identity not found.'}), 404

@app.route('/api/new_game', methods=['POST'])
def new_game():
    data = request.get_json(force=True)
    bet = int(data.get('bet', 10))
    username = session['username']
    
    if username not in USERS_DB: username = 'guest'
    if bet > USERS_DB[username]['balance'] or bet <= 0:
        return jsonify({'error': 'Transaction aborted: Insufficient vault balance.'}), 400
        
    deck = [{'suit': s, 'rank': r} for s in SUITS for r in RANKS]
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    session['deck'] = deck
    session['player_hand'] = player_hand
    session['dealer_hand'] = dealer_hand
    session['bet'] = bet
    session['game_over'] = False
    
    player_score = calculate_score(player_hand)
    if player_score == 21:
        USERS_DB[username]['balance'] += int(bet * 1.5)
        session['game_over'] = True
        return jsonify(get_game_state('Natural Blackjack! Payout executed.', True))

    return jsonify(get_game_state())

@app.route('/api/hit', methods=['POST'])
def hit():
    if session.get('game_over', True): return jsonify({'error': 'Active simulation not found.'}), 400
    username = session['username']
    
    deck = session['deck']
    player_hand = session['player_hand']
    player_hand.append(deck.pop())
    
    session['player_hand'] = player_hand
    session['deck'] = deck
    
    score = calculate_score(player_hand)
    if score > 21:
        USERS_DB[username]['balance'] -= session['bet']
        session['game_over'] = True
        return jsonify(get_game_state('Bust condition reached. House wins.', True))
        
    return jsonify(get_game_state())

@app.route('/api/stand', methods=['POST'])
def stand():
    if session.get('game_over', True): return jsonify({'error': 'Active simulation not found.'}), 400
    username = session['username']
    
    deck = session['deck']
    dealer_hand = session['dealer_hand']
    player_hand = session['player_hand']
    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)
        
    session['dealer_hand'] = dealer_hand
    session['game_over'] = True
    
    bet = session['bet']
    if dealer_score > 21:
        USERS_DB[username]['balance'] += bet
        status = 'Dealer busted. Liquidity transferred to Player.'
    elif player_score > dealer_score:
        USERS_DB[username]['balance'] += bet
        status = 'Player dominance established. You win.'
    elif player_score < dealer_score:
        USERS_DB[username]['balance'] -= bet
        status = 'House strategy superior. Dealer wins.'
    else:
        status = 'Stand-off detected. Wager returned to balance.'
        
    return jsonify(get_game_state(status, True))

def get_game_state(status="", show_all_dealer=False):
    username = session['username']
    dealer_hand = session['dealer_hand']
    visible_dealer_hand = dealer_hand if show_all_dealer else [dealer_hand[0], {'suit': '?', 'rank': '?'}]
    
    return {
        'player_hand': session['player_hand'],
        'dealer_hand': visible_dealer_hand,
        'player_score': calculate_score(session['player_hand']),
        'dealer_score': calculate_score(visible_dealer_hand) if not show_all_dealer else calculate_score(dealer_hand),
        'balance': USERS_DB[username]['balance'],
        'bet': session['bet'],
        'game_over': session['game_over'],
        'status': status
    }

if __name__ == '__main__':
    port = random.randint(5000, 9000)
    print(f"\n⚡ IBM CASINO NEXT-GEN RUNNING ON PORT: {port}")
    app.run(host='0.0.0.0', port=port, debug=True)

