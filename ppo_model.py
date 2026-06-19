import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical

class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim=3):
        super(ActorCritic, self).__init__()
        
        # רשת רחבה וכבדה משמעותית (256 נוירונים) למניעת צוואר בקבוק של מידע
        self.shared_layer = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.LayerNorm(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, 256),
            nn.LayerNorm(256),
            nn.ReLU()
        )
        
        self.actor_action_head = nn.Linear(256, action_dim)
        self.actor_size_head = nn.Sequential(
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )
        self.critic_head = nn.Linear(256, 1)
        
    def forward(self, state):
        features = self.shared_layer(state)
        action_probs = F.softmax(self.actor_action_head(features), dim=-1)
        position_size = self.actor_size_head(features)
        state_value = self.critic_head(features)
        return action_probs, position_size, state_value

