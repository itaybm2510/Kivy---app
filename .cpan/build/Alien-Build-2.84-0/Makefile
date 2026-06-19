# This Makefile is for the Alien::Build extension to perl.
#
# It was generated automatically by MakeMaker version
# 7.76 (Revision: 77600) from the contents of
# Makefile.PL. Don't edit this file, edit Makefile.PL instead.
#
#       ANY CHANGES MADE HERE WILL BE LOST!
#
#   MakeMaker ARGV: ()
#

#   MakeMaker Parameters:

#     ABSTRACT => q[Build external dependencies for use in CPAN]
#     AUTHOR => [q[Graham Ollis <plicease@cpan.org>, Joel Berger <joel.a.berger@gmail.com>]]
#     BUILD_REQUIRES => { ExtUtils::MakeMaker=>q[6.64] }
#     CONFIGURE_REQUIRES => { ExtUtils::CBuilder=>q[0], ExtUtils::MakeMaker=>q[6.64], ExtUtils::ParseXS=>q[3.30], File::Which=>q[0] }
#     DISTNAME => q[Alien-Build]
#     LICENSE => q[perl]
#     MIN_PERL_VERSION => q[5.008004]
#     NAME => q[Alien::Build]
#     PM => { lib/Alien/Base.pm=>q[$(INST_LIB)/Alien/Base.pm], lib/Alien/Base/Authoring.pod=>q[$(INST_LIB)/Alien/Base/Authoring.pod], lib/Alien/Base/FAQ.pod=>q[$(INST_LIB)/Alien/Base/FAQ.pod], lib/Alien/Base/PkgConfig.pm=>q[$(INST_LIB)/Alien/Base/PkgConfig.pm], lib/Alien/Base/Wrapper.pm=>q[$(INST_LIB)/Alien/Base/Wrapper.pm], lib/Alien/Build.pm=>q[$(INST_LIB)/Alien/Build.pm], lib/Alien/Build/CommandSequence.pm=>q[$(INST_LIB)/Alien/Build/CommandSequence.pm], lib/Alien/Build/Interpolate.pm=>q[$(INST_LIB)/Alien/Build/Interpolate.pm], lib/Alien/Build/Interpolate/Default.pm=>q[$(INST_LIB)/Alien/Build/Interpolate/Default.pm], lib/Alien/Build/Log.pm=>q[$(INST_LIB)/Alien/Build/Log.pm], lib/Alien/Build/Log/Abbreviate.pm=>q[$(INST_LIB)/Alien/Build/Log/Abbreviate.pm], lib/Alien/Build/Log/Default.pm=>q[$(INST_LIB)/Alien/Build/Log/Default.pm], lib/Alien/Build/MM.pm=>q[$(INST_LIB)/Alien/Build/MM.pm], lib/Alien/Build/Manual.pod=>q[$(INST_LIB)/Alien/Build/Manual.pod], lib/Alien/Build/Manual/Alien.pod=>q[$(INST_LIB)/Alien/Build/Manual/Alien.pod], lib/Alien/Build/Manual/AlienAuthor.pod=>q[$(INST_LIB)/Alien/Build/Manual/AlienAuthor.pod], lib/Alien/Build/Manual/AlienUser.pod=>q[$(INST_LIB)/Alien/Build/Manual/AlienUser.pod], lib/Alien/Build/Manual/Contributing.pod=>q[$(INST_LIB)/Alien/Build/Manual/Contributing.pod], lib/Alien/Build/Manual/FAQ.pod=>q[$(INST_LIB)/Alien/Build/Manual/FAQ.pod], lib/Alien/Build/Manual/PluginAuthor.pod=>q[$(INST_LIB)/Alien/Build/Manual/PluginAuthor.pod], lib/Alien/Build/Manual/Security.pod=>q[$(INST_LIB)/Alien/Build/Manual/Security.pod], lib/Alien/Build/Plugin.pm=>q[$(INST_LIB)/Alien/Build/Plugin.pm], lib/Alien/Build/Plugin/Build.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Build.pod], lib/Alien/Build/Plugin/Build/Autoconf.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Build/Autoconf.pm], lib/Alien/Build/Plugin/Build/CMake.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Build/CMake.pm], lib/Alien/Build/Plugin/Build/Copy.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Build/Copy.pm], lib/Alien/Build/Plugin/Build/MSYS.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Build/MSYS.pm], lib/Alien/Build/Plugin/Build/Make.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Build/Make.pm], lib/Alien/Build/Plugin/Build/SearchDep.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Build/SearchDep.pm], lib/Alien/Build/Plugin/Core.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Core.pod], lib/Alien/Build/Plugin/Core/CleanInstall.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/CleanInstall.pm], lib/Alien/Build/Plugin/Core/Download.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/Download.pm], lib/Alien/Build/Plugin/Core/FFI.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/FFI.pm], lib/Alien/Build/Plugin/Core/Gather.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/Gather.pm], lib/Alien/Build/Plugin/Core/Legacy.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/Legacy.pm], lib/Alien/Build/Plugin/Core/Override.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/Override.pm], lib/Alien/Build/Plugin/Core/Setup.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/Setup.pm], lib/Alien/Build/Plugin/Core/Tail.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Core/Tail.pm], lib/Alien/Build/Plugin/Decode.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Decode.pod], lib/Alien/Build/Plugin/Decode/DirListing.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Decode/DirListing.pm], lib/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm], lib/Alien/Build/Plugin/Decode/HTML.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Decode/HTML.pm], lib/Alien/Build/Plugin/Decode/Mojo.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Decode/Mojo.pm], lib/Alien/Build/Plugin/Digest.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Digest.pod], lib/Alien/Build/Plugin/Digest/Negotiate.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Digest/Negotiate.pm], lib/Alien/Build/Plugin/Digest/SHA.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Digest/SHA.pm], lib/Alien/Build/Plugin/Digest/SHAPP.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Digest/SHAPP.pm], lib/Alien/Build/Plugin/Download.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Download.pod], lib/Alien/Build/Plugin/Download/Negotiate.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Download/Negotiate.pm], lib/Alien/Build/Plugin/Extract.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Extract.pod], lib/Alien/Build/Plugin/Extract/ArchiveTar.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Extract/ArchiveTar.pm], lib/Alien/Build/Plugin/Extract/ArchiveZip.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Extract/ArchiveZip.pm], lib/Alien/Build/Plugin/Extract/CommandLine.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Extract/CommandLine.pm], lib/Alien/Build/Plugin/Extract/Directory.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Extract/Directory.pm], lib/Alien/Build/Plugin/Extract/File.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Extract/File.pm], lib/Alien/Build/Plugin/Extract/Negotiate.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Extract/Negotiate.pm], lib/Alien/Build/Plugin/Fetch.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch.pod], lib/Alien/Build/Plugin/Fetch/CurlCommand.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/CurlCommand.pm], lib/Alien/Build/Plugin/Fetch/HTTPTiny.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/HTTPTiny.pm], lib/Alien/Build/Plugin/Fetch/LWP.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/LWP.pm], lib/Alien/Build/Plugin/Fetch/Local.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/Local.pm], lib/Alien/Build/Plugin/Fetch/LocalDir.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/LocalDir.pm], lib/Alien/Build/Plugin/Fetch/NetFTP.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/NetFTP.pm], lib/Alien/Build/Plugin/Fetch/Wget.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Fetch/Wget.pm], lib/Alien/Build/Plugin/Gather.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Gather.pod], lib/Alien/Build/Plugin/Gather/IsolateDynamic.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Gather/IsolateDynamic.pm], lib/Alien/Build/Plugin/PkgConfig.pod=>q[$(INST_LIB)/Alien/Build/Plugin/PkgConfig.pod], lib/Alien/Build/Plugin/PkgConfig/CommandLine.pm=>q[$(INST_LIB)/Alien/Build/Plugin/PkgConfig/CommandLine.pm], lib/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm=>q[$(INST_LIB)/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm], lib/Alien/Build/Plugin/PkgConfig/MakeStatic.pm=>q[$(INST_LIB)/Alien/Build/Plugin/PkgConfig/MakeStatic.pm], lib/Alien/Build/Plugin/PkgConfig/Negotiate.pm=>q[$(INST_LIB)/Alien/Build/Plugin/PkgConfig/Negotiate.pm], lib/Alien/Build/Plugin/PkgConfig/PP.pm=>q[$(INST_LIB)/Alien/Build/Plugin/PkgConfig/PP.pm], lib/Alien/Build/Plugin/Prefer.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Prefer.pod], lib/Alien/Build/Plugin/Prefer/BadVersion.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Prefer/BadVersion.pm], lib/Alien/Build/Plugin/Prefer/GoodVersion.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Prefer/GoodVersion.pm], lib/Alien/Build/Plugin/Prefer/SortVersions.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Prefer/SortVersions.pm], lib/Alien/Build/Plugin/Probe.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Probe.pod], lib/Alien/Build/Plugin/Probe/CBuilder.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Probe/CBuilder.pm], lib/Alien/Build/Plugin/Probe/CommandLine.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Probe/CommandLine.pm], lib/Alien/Build/Plugin/Probe/Vcpkg.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Probe/Vcpkg.pm], lib/Alien/Build/Plugin/Test.pod=>q[$(INST_LIB)/Alien/Build/Plugin/Test.pod], lib/Alien/Build/Plugin/Test/Mock.pm=>q[$(INST_LIB)/Alien/Build/Plugin/Test/Mock.pm], lib/Alien/Build/Temp.pm=>q[$(INST_LIB)/Alien/Build/Temp.pm], lib/Alien/Build/Util.pm=>q[$(INST_LIB)/Alien/Build/Util.pm], lib/Alien/Build/Version/Basic.pm=>q[$(INST_LIB)/Alien/Build/Version/Basic.pm], lib/Alien/Build/rc.pm=>q[$(INST_LIB)/Alien/Build/rc.pm], lib/Alien/Role.pm=>q[$(INST_LIB)/Alien/Role.pm], lib/Alien/Util.pm=>q[$(INST_LIB)/Alien/Util.pm], lib/Test/Alien.pm=>q[$(INST_LIB)/Test/Alien.pm], lib/Test/Alien/Build.pm=>q[$(INST_LIB)/Test/Alien/Build.pm], lib/Test/Alien/CanCompile.pm=>q[$(INST_LIB)/Test/Alien/CanCompile.pm], lib/Test/Alien/CanPlatypus.pm=>q[$(INST_LIB)/Test/Alien/CanPlatypus.pm], lib/Test/Alien/Diag.pm=>q[$(INST_LIB)/Test/Alien/Diag.pm], lib/Test/Alien/Run.pm=>q[$(INST_LIB)/Test/Alien/Run.pm], lib/Test/Alien/Synthetic.pm=>q[$(INST_LIB)/Test/Alien/Synthetic.pm], lib/alienfile.pm=>q[$(INST_LIB)/alienfile.pm] }
#     PREREQ_PM => { Capture::Tiny=>q[0.17], Digest::SHA=>q[0], ExtUtils::CBuilder=>q[0], ExtUtils::MakeMaker=>q[6.64], ExtUtils::ParseXS=>q[3.30], FFI::CheckLib=>q[0.11], File::Which=>q[1.10], File::chdir=>q[0], JSON::PP=>q[0], List::Util=>q[1.33], Path::Tiny=>q[0.077], Test2::API=>q[1.302096], Test2::V0=>q[0.000121], Text::ParseWords=>q[3.26], parent=>q[0] }
#     TEST_REQUIRES => { Test2::API=>q[1.302096], Test2::V0=>q[0.000121] }
#     VERSION => q[2.84]
#     clean => { FILES=>q[.tmp] }
#     test => { TESTS=>q[t/*.t] }

# --- MakeMaker post_initialize section:


# --- MakeMaker const_config section:

# These definitions are from config.sh (via /data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android/Config.pm).
# They may have been overridden via Makefile.PL or on the command line.
AR = llvm-ar
CC = aarch64-linux-android-clang
CCCDLFLAGS = -fPIC -Wno-unused-function
CCDLFLAGS = -Wl,-E
CPPRUN = aarch64-linux-android-clang -E -P
DLEXT = so
DLSRC = dl_dlopen.xs
EXE_EXT = 
FULL_AR = ar
LD = aarch64-linux-android-clang -Wl,-rpath=/data/data/com.termux/files/usr/lib -Wl,--enable-new-dtags
LDDLFLAGS = -I/data/data/com.termux/files/usr/include -shared -I/data/data/com.termux/files/usr/include -Wl,-rpath=/data/data/com.termux/files/usr/lib -L/data/data/com.termux/files/usr/lib -landroid-utimes -lm
LDFLAGS = -I/data/data/com.termux/files/usr/include -Wl,-rpath=/data/data/com.termux/files/usr/lib -L/data/data/com.termux/files/usr/lib -landroid-utimes -lm
LIBC = 
LIB_EXT = .a
OBJ_EXT = .o
OSNAME = android
OSVERS = current
RANLIB = llvm-ranlib
SITELIBEXP = /data/data/com.termux/files/usr/lib/perl5/site_perl/5.42.0
SITEARCHEXP = /data/data/com.termux/files/usr/lib/perl5/site_perl/5.42.0/aarch64-android
SO = so
VENDORARCHEXP = 
VENDORLIBEXP = 


# --- MakeMaker constants section:
AR_STATIC_ARGS = cr
DIRFILESEP = /
DFSEP = $(DIRFILESEP)
NAME = Alien::Build
NAME_SYM = Alien_Build
VERSION = 2.84
VERSION_MACRO = VERSION
VERSION_SYM = 2_84
DEFINE_VERSION = -D$(VERSION_MACRO)=\"$(VERSION)\"
XS_VERSION = 2.84
XS_VERSION_MACRO = XS_VERSION
XS_DEFINE_VERSION = -D$(XS_VERSION_MACRO)=\"$(XS_VERSION)\"
INST_ARCHLIB = blib/arch
INST_SCRIPT = blib/script
INST_BIN = blib/bin
INST_LIB = blib/lib
INST_MAN1DIR = blib/man1
INST_MAN3DIR = blib/man3
MAN1EXT = 1
MAN3EXT = 3
MAN1SECTION = 1
MAN3SECTION = 3
INSTALLDIRS = site
DESTDIR = 
PREFIX = $(SITEPREFIX)
PERLPREFIX = /data/data/com.termux/files/usr
SITEPREFIX = /data/data/com.termux/files/usr
VENDORPREFIX = 
INSTALLPRIVLIB = /data/data/com.termux/files/usr/lib/perl5/5.42.0
DESTINSTALLPRIVLIB = $(DESTDIR)$(INSTALLPRIVLIB)
INSTALLSITELIB = /data/data/com.termux/files/usr/lib/perl5/site_perl/5.42.0
DESTINSTALLSITELIB = $(DESTDIR)$(INSTALLSITELIB)
INSTALLVENDORLIB = 
DESTINSTALLVENDORLIB = $(DESTDIR)$(INSTALLVENDORLIB)
INSTALLARCHLIB = /data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android
DESTINSTALLARCHLIB = $(DESTDIR)$(INSTALLARCHLIB)
INSTALLSITEARCH = /data/data/com.termux/files/usr/lib/perl5/site_perl/5.42.0/aarch64-android
DESTINSTALLSITEARCH = $(DESTDIR)$(INSTALLSITEARCH)
INSTALLVENDORARCH = 
DESTINSTALLVENDORARCH = $(DESTDIR)$(INSTALLVENDORARCH)
INSTALLBIN = /data/data/com.termux/files/usr/bin
DESTINSTALLBIN = $(DESTDIR)$(INSTALLBIN)
INSTALLSITEBIN = /data/data/com.termux/files/usr/bin
DESTINSTALLSITEBIN = $(DESTDIR)$(INSTALLSITEBIN)
INSTALLVENDORBIN = 
DESTINSTALLVENDORBIN = $(DESTDIR)$(INSTALLVENDORBIN)
INSTALLSCRIPT = /data/data/com.termux/files/usr/bin
DESTINSTALLSCRIPT = $(DESTDIR)$(INSTALLSCRIPT)
INSTALLSITESCRIPT = /data/data/com.termux/files/usr/bin
DESTINSTALLSITESCRIPT = $(DESTDIR)$(INSTALLSITESCRIPT)
INSTALLVENDORSCRIPT = 
DESTINSTALLVENDORSCRIPT = $(DESTDIR)$(INSTALLVENDORSCRIPT)
INSTALLMAN1DIR = /data/data/com.termux/files/usr/share/man/man1
DESTINSTALLMAN1DIR = $(DESTDIR)$(INSTALLMAN1DIR)
INSTALLSITEMAN1DIR = /data/data/com.termux/files/usr/share/man/man1
DESTINSTALLSITEMAN1DIR = $(DESTDIR)$(INSTALLSITEMAN1DIR)
INSTALLVENDORMAN1DIR = 
DESTINSTALLVENDORMAN1DIR = $(DESTDIR)$(INSTALLVENDORMAN1DIR)
INSTALLMAN3DIR = /data/data/com.termux/files/usr/share/man/man3
DESTINSTALLMAN3DIR = $(DESTDIR)$(INSTALLMAN3DIR)
INSTALLSITEMAN3DIR = /data/data/com.termux/files/usr/share/man/man3
DESTINSTALLSITEMAN3DIR = $(DESTDIR)$(INSTALLSITEMAN3DIR)
INSTALLVENDORMAN3DIR = 
DESTINSTALLVENDORMAN3DIR = $(DESTDIR)$(INSTALLVENDORMAN3DIR)
PERL_LIB = /data/data/com.termux/files/usr/lib/perl5/5.42.0
PERL_ARCHLIB = /data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android
LIBPERL_A = libperl.a
FIRST_MAKEFILE = Makefile
MAKEFILE_OLD = Makefile.old
MAKE_APERL_FILE = Makefile.aperl
PERLMAINCC = $(CC)
PERL_INC = /data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android/CORE
PERL = "/data/data/com.termux/files/usr/bin/perl"
FULLPERL = "/data/data/com.termux/files/usr/bin/perl"
ABSPERL = $(PERL)
PERLRUN = $(PERL)
FULLPERLRUN = $(FULLPERL)
ABSPERLRUN = $(ABSPERL)
PERLRUNINST = $(PERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
FULLPERLRUNINST = $(FULLPERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
ABSPERLRUNINST = $(ABSPERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
PERL_CORE = 0
PERM_DIR = 755
PERM_RW = 644
PERM_RWX = 755

MAKEMAKER   = /data/data/com.termux/files/usr/lib/perl5/5.42.0/ExtUtils/MakeMaker.pm
MM_VERSION  = 7.76
MM_REVISION = 77600

# FULLEXT = Pathname for extension directory (eg Foo/Bar/Oracle).
# BASEEXT = Basename part of FULLEXT. May be just equal FULLEXT. (eg Oracle)
# PARENT_NAME = NAME without BASEEXT and no trailing :: (eg Foo::Bar)
# DLBASE  = Basename part of dynamic library. May be just equal BASEEXT.
MAKE = make
FULLEXT = Alien/Build
BASEEXT = Build
PARENT_NAME = Alien
DLBASE = $(BASEEXT)
VERSION_FROM = 
OBJECT = 
LDFROM = $(OBJECT)
LINKTYPE = dynamic
BOOTDEP = 

# Handy lists of source code files:
XS_FILES = 
C_FILES  = 
O_FILES  = 
H_FILES  = 
MAN1PODS = 
MAN3PODS = lib/Alien/Base.pm \
	lib/Alien/Base/Authoring.pod \
	lib/Alien/Base/FAQ.pod \
	lib/Alien/Base/PkgConfig.pm \
	lib/Alien/Base/Wrapper.pm \
	lib/Alien/Build.pm \
	lib/Alien/Build/CommandSequence.pm \
	lib/Alien/Build/Interpolate.pm \
	lib/Alien/Build/Interpolate/Default.pm \
	lib/Alien/Build/Log.pm \
	lib/Alien/Build/Log/Abbreviate.pm \
	lib/Alien/Build/Log/Default.pm \
	lib/Alien/Build/MM.pm \
	lib/Alien/Build/Manual.pod \
	lib/Alien/Build/Manual/Alien.pod \
	lib/Alien/Build/Manual/AlienAuthor.pod \
	lib/Alien/Build/Manual/AlienUser.pod \
	lib/Alien/Build/Manual/Contributing.pod \
	lib/Alien/Build/Manual/FAQ.pod \
	lib/Alien/Build/Manual/PluginAuthor.pod \
	lib/Alien/Build/Manual/Security.pod \
	lib/Alien/Build/Plugin.pm \
	lib/Alien/Build/Plugin/Build.pod \
	lib/Alien/Build/Plugin/Build/Autoconf.pm \
	lib/Alien/Build/Plugin/Build/CMake.pm \
	lib/Alien/Build/Plugin/Build/Copy.pm \
	lib/Alien/Build/Plugin/Build/MSYS.pm \
	lib/Alien/Build/Plugin/Build/Make.pm \
	lib/Alien/Build/Plugin/Build/SearchDep.pm \
	lib/Alien/Build/Plugin/Core.pod \
	lib/Alien/Build/Plugin/Core/CleanInstall.pm \
	lib/Alien/Build/Plugin/Core/Download.pm \
	lib/Alien/Build/Plugin/Core/FFI.pm \
	lib/Alien/Build/Plugin/Core/Gather.pm \
	lib/Alien/Build/Plugin/Core/Legacy.pm \
	lib/Alien/Build/Plugin/Core/Override.pm \
	lib/Alien/Build/Plugin/Core/Setup.pm \
	lib/Alien/Build/Plugin/Core/Tail.pm \
	lib/Alien/Build/Plugin/Decode.pod \
	lib/Alien/Build/Plugin/Decode/DirListing.pm \
	lib/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm \
	lib/Alien/Build/Plugin/Decode/HTML.pm \
	lib/Alien/Build/Plugin/Decode/Mojo.pm \
	lib/Alien/Build/Plugin/Digest.pod \
	lib/Alien/Build/Plugin/Digest/Negotiate.pm \
	lib/Alien/Build/Plugin/Digest/SHA.pm \
	lib/Alien/Build/Plugin/Digest/SHAPP.pm \
	lib/Alien/Build/Plugin/Download.pod \
	lib/Alien/Build/Plugin/Download/Negotiate.pm \
	lib/Alien/Build/Plugin/Extract.pod \
	lib/Alien/Build/Plugin/Extract/ArchiveTar.pm \
	lib/Alien/Build/Plugin/Extract/ArchiveZip.pm \
	lib/Alien/Build/Plugin/Extract/CommandLine.pm \
	lib/Alien/Build/Plugin/Extract/Directory.pm \
	lib/Alien/Build/Plugin/Extract/File.pm \
	lib/Alien/Build/Plugin/Extract/Negotiate.pm \
	lib/Alien/Build/Plugin/Fetch.pod \
	lib/Alien/Build/Plugin/Fetch/CurlCommand.pm \
	lib/Alien/Build/Plugin/Fetch/HTTPTiny.pm \
	lib/Alien/Build/Plugin/Fetch/LWP.pm \
	lib/Alien/Build/Plugin/Fetch/Local.pm \
	lib/Alien/Build/Plugin/Fetch/LocalDir.pm \
	lib/Alien/Build/Plugin/Fetch/NetFTP.pm \
	lib/Alien/Build/Plugin/Fetch/Wget.pm \
	lib/Alien/Build/Plugin/Gather.pod \
	lib/Alien/Build/Plugin/Gather/IsolateDynamic.pm \
	lib/Alien/Build/Plugin/PkgConfig.pod \
	lib/Alien/Build/Plugin/PkgConfig/CommandLine.pm \
	lib/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm \
	lib/Alien/Build/Plugin/PkgConfig/MakeStatic.pm \
	lib/Alien/Build/Plugin/PkgConfig/Negotiate.pm \
	lib/Alien/Build/Plugin/PkgConfig/PP.pm \
	lib/Alien/Build/Plugin/Prefer.pod \
	lib/Alien/Build/Plugin/Prefer/BadVersion.pm \
	lib/Alien/Build/Plugin/Prefer/GoodVersion.pm \
	lib/Alien/Build/Plugin/Prefer/SortVersions.pm \
	lib/Alien/Build/Plugin/Probe.pod \
	lib/Alien/Build/Plugin/Probe/CBuilder.pm \
	lib/Alien/Build/Plugin/Probe/CommandLine.pm \
	lib/Alien/Build/Plugin/Probe/Vcpkg.pm \
	lib/Alien/Build/Plugin/Test.pod \
	lib/Alien/Build/Plugin/Test/Mock.pm \
	lib/Alien/Build/Temp.pm \
	lib/Alien/Build/Util.pm \
	lib/Alien/Build/Version/Basic.pm \
	lib/Alien/Build/rc.pm \
	lib/Alien/Role.pm \
	lib/Alien/Util.pm \
	lib/Test/Alien.pm \
	lib/Test/Alien/Build.pm \
	lib/Test/Alien/CanCompile.pm \
	lib/Test/Alien/CanPlatypus.pm \
	lib/Test/Alien/Diag.pm \
	lib/Test/Alien/Run.pm \
	lib/Test/Alien/Synthetic.pm \
	lib/alienfile.pm

# Where to build things
INST_LIBDIR      = $(INST_LIB)/Alien
INST_ARCHLIBDIR  = $(INST_ARCHLIB)/Alien

INST_AUTODIR     = $(INST_LIB)/auto/$(FULLEXT)
INST_ARCHAUTODIR = $(INST_ARCHLIB)/auto/$(FULLEXT)

INST_STATIC      = 
INST_DYNAMIC     = 
INST_BOOT        = 

# Extra linker info
EXPORT_LIST        = 
PERL_ARCHIVE       = 
PERL_ARCHIVE_AFTER = 


TO_INST_PM = lib/Alien/Base.pm \
	lib/Alien/Base/Authoring.pod \
	lib/Alien/Base/FAQ.pod \
	lib/Alien/Base/PkgConfig.pm \
	lib/Alien/Base/Wrapper.pm \
	lib/Alien/Build.pm \
	lib/Alien/Build/CommandSequence.pm \
	lib/Alien/Build/Interpolate.pm \
	lib/Alien/Build/Interpolate/Default.pm \
	lib/Alien/Build/Log.pm \
	lib/Alien/Build/Log/Abbreviate.pm \
	lib/Alien/Build/Log/Default.pm \
	lib/Alien/Build/MM.pm \
	lib/Alien/Build/Manual.pod \
	lib/Alien/Build/Manual/Alien.pod \
	lib/Alien/Build/Manual/AlienAuthor.pod \
	lib/Alien/Build/Manual/AlienUser.pod \
	lib/Alien/Build/Manual/Contributing.pod \
	lib/Alien/Build/Manual/FAQ.pod \
	lib/Alien/Build/Manual/PluginAuthor.pod \
	lib/Alien/Build/Manual/Security.pod \
	lib/Alien/Build/Plugin.pm \
	lib/Alien/Build/Plugin/Build.pod \
	lib/Alien/Build/Plugin/Build/Autoconf.pm \
	lib/Alien/Build/Plugin/Build/CMake.pm \
	lib/Alien/Build/Plugin/Build/Copy.pm \
	lib/Alien/Build/Plugin/Build/MSYS.pm \
	lib/Alien/Build/Plugin/Build/Make.pm \
	lib/Alien/Build/Plugin/Build/SearchDep.pm \
	lib/Alien/Build/Plugin/Core.pod \
	lib/Alien/Build/Plugin/Core/CleanInstall.pm \
	lib/Alien/Build/Plugin/Core/Download.pm \
	lib/Alien/Build/Plugin/Core/FFI.pm \
	lib/Alien/Build/Plugin/Core/Gather.pm \
	lib/Alien/Build/Plugin/Core/Legacy.pm \
	lib/Alien/Build/Plugin/Core/Override.pm \
	lib/Alien/Build/Plugin/Core/Setup.pm \
	lib/Alien/Build/Plugin/Core/Tail.pm \
	lib/Alien/Build/Plugin/Decode.pod \
	lib/Alien/Build/Plugin/Decode/DirListing.pm \
	lib/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm \
	lib/Alien/Build/Plugin/Decode/HTML.pm \
	lib/Alien/Build/Plugin/Decode/Mojo.pm \
	lib/Alien/Build/Plugin/Digest.pod \
	lib/Alien/Build/Plugin/Digest/Negotiate.pm \
	lib/Alien/Build/Plugin/Digest/SHA.pm \
	lib/Alien/Build/Plugin/Digest/SHAPP.pm \
	lib/Alien/Build/Plugin/Download.pod \
	lib/Alien/Build/Plugin/Download/Negotiate.pm \
	lib/Alien/Build/Plugin/Extract.pod \
	lib/Alien/Build/Plugin/Extract/ArchiveTar.pm \
	lib/Alien/Build/Plugin/Extract/ArchiveZip.pm \
	lib/Alien/Build/Plugin/Extract/CommandLine.pm \
	lib/Alien/Build/Plugin/Extract/Directory.pm \
	lib/Alien/Build/Plugin/Extract/File.pm \
	lib/Alien/Build/Plugin/Extract/Negotiate.pm \
	lib/Alien/Build/Plugin/Fetch.pod \
	lib/Alien/Build/Plugin/Fetch/CurlCommand.pm \
	lib/Alien/Build/Plugin/Fetch/HTTPTiny.pm \
	lib/Alien/Build/Plugin/Fetch/LWP.pm \
	lib/Alien/Build/Plugin/Fetch/Local.pm \
	lib/Alien/Build/Plugin/Fetch/LocalDir.pm \
	lib/Alien/Build/Plugin/Fetch/NetFTP.pm \
	lib/Alien/Build/Plugin/Fetch/Wget.pm \
	lib/Alien/Build/Plugin/Gather.pod \
	lib/Alien/Build/Plugin/Gather/IsolateDynamic.pm \
	lib/Alien/Build/Plugin/PkgConfig.pod \
	lib/Alien/Build/Plugin/PkgConfig/CommandLine.pm \
	lib/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm \
	lib/Alien/Build/Plugin/PkgConfig/MakeStatic.pm \
	lib/Alien/Build/Plugin/PkgConfig/Negotiate.pm \
	lib/Alien/Build/Plugin/PkgConfig/PP.pm \
	lib/Alien/Build/Plugin/Prefer.pod \
	lib/Alien/Build/Plugin/Prefer/BadVersion.pm \
	lib/Alien/Build/Plugin/Prefer/GoodVersion.pm \
	lib/Alien/Build/Plugin/Prefer/SortVersions.pm \
	lib/Alien/Build/Plugin/Probe.pod \
	lib/Alien/Build/Plugin/Probe/CBuilder.pm \
	lib/Alien/Build/Plugin/Probe/CommandLine.pm \
	lib/Alien/Build/Plugin/Probe/Vcpkg.pm \
	lib/Alien/Build/Plugin/Test.pod \
	lib/Alien/Build/Plugin/Test/Mock.pm \
	lib/Alien/Build/Temp.pm \
	lib/Alien/Build/Util.pm \
	lib/Alien/Build/Version/Basic.pm \
	lib/Alien/Build/rc.pm \
	lib/Alien/Role.pm \
	lib/Alien/Util.pm \
	lib/Test/Alien.pm \
	lib/Test/Alien/Build.pm \
	lib/Test/Alien/CanCompile.pm \
	lib/Test/Alien/CanPlatypus.pm \
	lib/Test/Alien/Diag.pm \
	lib/Test/Alien/Run.pm \
	lib/Test/Alien/Synthetic.pm \
	lib/alienfile.pm
PERL_ARCHLIBDEP = /data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android
PERL_INCDEP = /data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android/CORE


# Dependencies info
PERL_ARCHIVEDEP    = 

# Where is the Config information that we are using/depend on
CONFIGDEP = $(PERL_ARCHLIBDEP)$(DFSEP)Config.pm $(PERL_INCDEP)$(DFSEP)config.h


# --- MakeMaker platform_constants section:
MM_Unix_VERSION = 7.76
PERL_MALLOC_DEF = -DPERL_EXTMALLOC_DEF -Dmalloc=Perl_malloc -Dfree=Perl_mfree -Drealloc=Perl_realloc -Dcalloc=Perl_calloc


# --- MakeMaker tool_autosplit section:
# Usage: $(AUTOSPLITFILE) FileToSplit AutoDirToSplitInto
AUTOSPLITFILE = $(ABSPERLRUN)  -e 'use AutoSplit;  autosplit($$$$ARGV[0], $$$$ARGV[1], 0, 1, 1)' --



# --- MakeMaker tool_xsubpp section:


# --- MakeMaker tools_other section:
SHELL = /data/data/com.termux/files/usr/bin/sh
CHMOD = chmod
CP = cp
MV = mv
NOOP = $(TRUE)
NOECHO = @
RM_F = rm -f
RM_RF = rm -rf
TEST_F = test -f
TOUCH = touch
UMASK_NULL = umask 0
DEV_NULL = > /dev/null 2>&1
MKPATH = $(ABSPERLRUN) -MExtUtils::Command -e 'mkpath' --
EQUALIZE_TIMESTAMP = $(ABSPERLRUN) -MExtUtils::Command -e 'eqtime' --
FALSE = false
TRUE = true
ECHO = echo
ECHO_N = echo -n
UNINST = 0
VERBINST = 0
MOD_INSTALL = $(ABSPERLRUN) -MExtUtils::Install -e 'install([ from_to => {@ARGV}, verbose => '\''$(VERBINST)'\'', uninstall_shadows => '\''$(UNINST)'\'', dir_mode => '\''$(PERM_DIR)'\'' ]);' --
DOC_INSTALL = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'perllocal_install' --
UNINSTALL = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'uninstall' --
WARN_IF_OLD_PACKLIST = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'warn_if_old_packlist' --
MACROSTART = 
MACROEND = 
USEMAKEFILE = -f
FIXIN = $(ABSPERLRUN) -MExtUtils::MY -e 'MY->fixin(shift)' --
CP_NONEMPTY = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'cp_nonempty' --


# --- MakeMaker makemakerdflt section:
makemakerdflt : all
	$(NOECHO) $(NOOP)


# --- MakeMaker dist section:
TAR = tar
TARFLAGS = cvf
ZIP = zip
ZIPFLAGS = -r
COMPRESS = gzip --best
SUFFIX = .gz
SHAR = shar
PREOP = $(NOECHO) $(NOOP)
POSTOP = $(NOECHO) $(NOOP)
TO_UNIX = $(NOECHO) $(NOOP)
CI = ci -u
RCS_LABEL = rcs -Nv$(VERSION_SYM): -q
DIST_CP = best
DIST_DEFAULT = tardist
DISTNAME = Alien-Build
DISTVNAME = Alien-Build-2.84


# --- MakeMaker macro section:


# --- MakeMaker depend section:


# --- MakeMaker cflags section:


# --- MakeMaker const_loadlibs section:


# --- MakeMaker const_cccmd section:


# --- MakeMaker post_constants section:


# --- MakeMaker pasthru section:

PASTHRU = LIBPERL_A="$(LIBPERL_A)"\
	LINKTYPE="$(LINKTYPE)"\
	PREFIX="$(PREFIX)"\
	PASTHRU_DEFINE='$(DEFINE) $(PASTHRU_DEFINE)'\
	PASTHRU_INC='$(INC) $(PASTHRU_INC)'


# --- MakeMaker special_targets section:
.SUFFIXES : .xs .c .C .cpp .i .s .cxx .cc $(OBJ_EXT)

.PHONY: all config static dynamic test linkext manifest blibdirs clean realclean disttest distdir pure_all subdirs clean_subdirs makemakerdflt manifypods realclean_subdirs subdirs_dynamic subdirs_pure_nolink subdirs_static subdirs-test_dynamic subdirs-test_static test_dynamic test_static



# --- MakeMaker c_o section:


# --- MakeMaker xs_c section:


# --- MakeMaker xs_o section:


# --- MakeMaker top_targets section:
all :: pure_all manifypods
	$(NOECHO) $(NOOP)

pure_all :: config pm_to_blib subdirs linkext
	$(NOECHO) $(NOOP)

subdirs :: $(MYEXTLIB)
	$(NOECHO) $(NOOP)

config :: $(FIRST_MAKEFILE) blibdirs
	$(NOECHO) $(NOOP)

help :
	perldoc ExtUtils::MakeMaker


# --- MakeMaker blibdirs section:
blibdirs : $(INST_LIBDIR)$(DFSEP).exists $(INST_ARCHLIB)$(DFSEP).exists $(INST_AUTODIR)$(DFSEP).exists $(INST_ARCHAUTODIR)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists $(INST_SCRIPT)$(DFSEP).exists $(INST_MAN1DIR)$(DFSEP).exists $(INST_MAN3DIR)$(DFSEP).exists
	$(NOECHO) $(NOOP)

# Backwards compat with 6.18 through 6.25
blibdirs.ts : blibdirs
	$(NOECHO) $(NOOP)

$(INST_LIBDIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_LIBDIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_LIBDIR)
	$(NOECHO) $(TOUCH) $(INST_LIBDIR)$(DFSEP).exists

$(INST_ARCHLIB)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_ARCHLIB)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_ARCHLIB)
	$(NOECHO) $(TOUCH) $(INST_ARCHLIB)$(DFSEP).exists

$(INST_AUTODIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_AUTODIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_AUTODIR)
	$(NOECHO) $(TOUCH) $(INST_AUTODIR)$(DFSEP).exists

$(INST_ARCHAUTODIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_ARCHAUTODIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_ARCHAUTODIR)
	$(NOECHO) $(TOUCH) $(INST_ARCHAUTODIR)$(DFSEP).exists

$(INST_BIN)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_BIN)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_BIN)
	$(NOECHO) $(TOUCH) $(INST_BIN)$(DFSEP).exists

$(INST_SCRIPT)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_SCRIPT)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_SCRIPT)
	$(NOECHO) $(TOUCH) $(INST_SCRIPT)$(DFSEP).exists

$(INST_MAN1DIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_MAN1DIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_MAN1DIR)
	$(NOECHO) $(TOUCH) $(INST_MAN1DIR)$(DFSEP).exists

$(INST_MAN3DIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_MAN3DIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_MAN3DIR)
	$(NOECHO) $(TOUCH) $(INST_MAN3DIR)$(DFSEP).exists



# --- MakeMaker linkext section:

linkext :: dynamic
	$(NOECHO) $(NOOP)


# --- MakeMaker dlsyms section:


# --- MakeMaker dynamic_bs section:

BOOTSTRAP =


# --- MakeMaker dynamic section:

dynamic :: $(FIRST_MAKEFILE) config $(INST_BOOT) $(INST_DYNAMIC)
	$(NOECHO) $(NOOP)


# --- MakeMaker dynamic_lib section:


# --- MakeMaker static section:

## $(INST_PM) has been moved to the all: target.
## It remains here for awhile to allow for old usage: "make static"
static :: $(FIRST_MAKEFILE) $(INST_STATIC)
	$(NOECHO) $(NOOP)


# --- MakeMaker static_lib section:


# --- MakeMaker manifypods section:

POD2MAN_EXE = $(PERLRUN) "-MExtUtils::Command::MM" -e pod2man "--"
POD2MAN = $(POD2MAN_EXE)


manifypods : pure_all config  \
	lib/Alien/Base.pm \
	lib/Alien/Base/Authoring.pod \
	lib/Alien/Base/FAQ.pod \
	lib/Alien/Base/PkgConfig.pm \
	lib/Alien/Base/Wrapper.pm \
	lib/Alien/Build.pm \
	lib/Alien/Build/CommandSequence.pm \
	lib/Alien/Build/Interpolate.pm \
	lib/Alien/Build/Interpolate/Default.pm \
	lib/Alien/Build/Log.pm \
	lib/Alien/Build/Log/Abbreviate.pm \
	lib/Alien/Build/Log/Default.pm \
	lib/Alien/Build/MM.pm \
	lib/Alien/Build/Manual.pod \
	lib/Alien/Build/Manual/Alien.pod \
	lib/Alien/Build/Manual/AlienAuthor.pod \
	lib/Alien/Build/Manual/AlienUser.pod \
	lib/Alien/Build/Manual/Contributing.pod \
	lib/Alien/Build/Manual/FAQ.pod \
	lib/Alien/Build/Manual/PluginAuthor.pod \
	lib/Alien/Build/Manual/Security.pod \
	lib/Alien/Build/Plugin.pm \
	lib/Alien/Build/Plugin/Build.pod \
	lib/Alien/Build/Plugin/Build/Autoconf.pm \
	lib/Alien/Build/Plugin/Build/CMake.pm \
	lib/Alien/Build/Plugin/Build/Copy.pm \
	lib/Alien/Build/Plugin/Build/MSYS.pm \
	lib/Alien/Build/Plugin/Build/Make.pm \
	lib/Alien/Build/Plugin/Build/SearchDep.pm \
	lib/Alien/Build/Plugin/Core.pod \
	lib/Alien/Build/Plugin/Core/CleanInstall.pm \
	lib/Alien/Build/Plugin/Core/Download.pm \
	lib/Alien/Build/Plugin/Core/FFI.pm \
	lib/Alien/Build/Plugin/Core/Gather.pm \
	lib/Alien/Build/Plugin/Core/Legacy.pm \
	lib/Alien/Build/Plugin/Core/Override.pm \
	lib/Alien/Build/Plugin/Core/Setup.pm \
	lib/Alien/Build/Plugin/Core/Tail.pm \
	lib/Alien/Build/Plugin/Decode.pod \
	lib/Alien/Build/Plugin/Decode/DirListing.pm \
	lib/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm \
	lib/Alien/Build/Plugin/Decode/HTML.pm \
	lib/Alien/Build/Plugin/Decode/Mojo.pm \
	lib/Alien/Build/Plugin/Digest.pod \
	lib/Alien/Build/Plugin/Digest/Negotiate.pm \
	lib/Alien/Build/Plugin/Digest/SHA.pm \
	lib/Alien/Build/Plugin/Digest/SHAPP.pm \
	lib/Alien/Build/Plugin/Download.pod \
	lib/Alien/Build/Plugin/Download/Negotiate.pm \
	lib/Alien/Build/Plugin/Extract.pod \
	lib/Alien/Build/Plugin/Extract/ArchiveTar.pm \
	lib/Alien/Build/Plugin/Extract/ArchiveZip.pm \
	lib/Alien/Build/Plugin/Extract/CommandLine.pm \
	lib/Alien/Build/Plugin/Extract/Directory.pm \
	lib/Alien/Build/Plugin/Extract/File.pm \
	lib/Alien/Build/Plugin/Extract/Negotiate.pm \
	lib/Alien/Build/Plugin/Fetch.pod \
	lib/Alien/Build/Plugin/Fetch/CurlCommand.pm \
	lib/Alien/Build/Plugin/Fetch/HTTPTiny.pm \
	lib/Alien/Build/Plugin/Fetch/LWP.pm \
	lib/Alien/Build/Plugin/Fetch/Local.pm \
	lib/Alien/Build/Plugin/Fetch/LocalDir.pm \
	lib/Alien/Build/Plugin/Fetch/NetFTP.pm \
	lib/Alien/Build/Plugin/Fetch/Wget.pm \
	lib/Alien/Build/Plugin/Gather.pod \
	lib/Alien/Build/Plugin/Gather/IsolateDynamic.pm \
	lib/Alien/Build/Plugin/PkgConfig.pod \
	lib/Alien/Build/Plugin/PkgConfig/CommandLine.pm \
	lib/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm \
	lib/Alien/Build/Plugin/PkgConfig/MakeStatic.pm \
	lib/Alien/Build/Plugin/PkgConfig/Negotiate.pm \
	lib/Alien/Build/Plugin/PkgConfig/PP.pm \
	lib/Alien/Build/Plugin/Prefer.pod \
	lib/Alien/Build/Plugin/Prefer/BadVersion.pm \
	lib/Alien/Build/Plugin/Prefer/GoodVersion.pm \
	lib/Alien/Build/Plugin/Prefer/SortVersions.pm \
	lib/Alien/Build/Plugin/Probe.pod \
	lib/Alien/Build/Plugin/Probe/CBuilder.pm \
	lib/Alien/Build/Plugin/Probe/CommandLine.pm \
	lib/Alien/Build/Plugin/Probe/Vcpkg.pm \
	lib/Alien/Build/Plugin/Test.pod \
	lib/Alien/Build/Plugin/Test/Mock.pm \
	lib/Alien/Build/Temp.pm \
	lib/Alien/Build/Util.pm \
	lib/Alien/Build/Version/Basic.pm \
	lib/Alien/Build/rc.pm \
	lib/Alien/Role.pm \
	lib/Alien/Util.pm \
	lib/Test/Alien.pm \
	lib/Test/Alien/Build.pm \
	lib/Test/Alien/CanCompile.pm \
	lib/Test/Alien/CanPlatypus.pm \
	lib/Test/Alien/Diag.pm \
	lib/Test/Alien/Run.pm \
	lib/Test/Alien/Synthetic.pm \
	lib/alienfile.pm
	$(NOECHO) $(POD2MAN) --section=$(MAN3SECTION) --perm_rw=$(PERM_RW) -u \
	  lib/Alien/Base.pm $(INST_MAN3DIR)/Alien::Base.$(MAN3EXT) \
	  lib/Alien/Base/Authoring.pod $(INST_MAN3DIR)/Alien::Base::Authoring.$(MAN3EXT) \
	  lib/Alien/Base/FAQ.pod $(INST_MAN3DIR)/Alien::Base::FAQ.$(MAN3EXT) \
	  lib/Alien/Base/PkgConfig.pm $(INST_MAN3DIR)/Alien::Base::PkgConfig.$(MAN3EXT) \
	  lib/Alien/Base/Wrapper.pm $(INST_MAN3DIR)/Alien::Base::Wrapper.$(MAN3EXT) \
	  lib/Alien/Build.pm $(INST_MAN3DIR)/Alien::Build.$(MAN3EXT) \
	  lib/Alien/Build/CommandSequence.pm $(INST_MAN3DIR)/Alien::Build::CommandSequence.$(MAN3EXT) \
	  lib/Alien/Build/Interpolate.pm $(INST_MAN3DIR)/Alien::Build::Interpolate.$(MAN3EXT) \
	  lib/Alien/Build/Interpolate/Default.pm $(INST_MAN3DIR)/Alien::Build::Interpolate::Default.$(MAN3EXT) \
	  lib/Alien/Build/Log.pm $(INST_MAN3DIR)/Alien::Build::Log.$(MAN3EXT) \
	  lib/Alien/Build/Log/Abbreviate.pm $(INST_MAN3DIR)/Alien::Build::Log::Abbreviate.$(MAN3EXT) \
	  lib/Alien/Build/Log/Default.pm $(INST_MAN3DIR)/Alien::Build::Log::Default.$(MAN3EXT) \
	  lib/Alien/Build/MM.pm $(INST_MAN3DIR)/Alien::Build::MM.$(MAN3EXT) \
	  lib/Alien/Build/Manual.pod $(INST_MAN3DIR)/Alien::Build::Manual.$(MAN3EXT) \
	  lib/Alien/Build/Manual/Alien.pod $(INST_MAN3DIR)/Alien::Build::Manual::Alien.$(MAN3EXT) \
	  lib/Alien/Build/Manual/AlienAuthor.pod $(INST_MAN3DIR)/Alien::Build::Manual::AlienAuthor.$(MAN3EXT) \
	  lib/Alien/Build/Manual/AlienUser.pod $(INST_MAN3DIR)/Alien::Build::Manual::AlienUser.$(MAN3EXT) \
	  lib/Alien/Build/Manual/Contributing.pod $(INST_MAN3DIR)/Alien::Build::Manual::Contributing.$(MAN3EXT) \
	  lib/Alien/Build/Manual/FAQ.pod $(INST_MAN3DIR)/Alien::Build::Manual::FAQ.$(MAN3EXT) \
	  lib/Alien/Build/Manual/PluginAuthor.pod $(INST_MAN3DIR)/Alien::Build::Manual::PluginAuthor.$(MAN3EXT) \
	  lib/Alien/Build/Manual/Security.pod $(INST_MAN3DIR)/Alien::Build::Manual::Security.$(MAN3EXT) \
	  lib/Alien/Build/Plugin.pm $(INST_MAN3DIR)/Alien::Build::Plugin.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Build.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build/Autoconf.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Build::Autoconf.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build/CMake.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Build::CMake.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build/Copy.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Build::Copy.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build/MSYS.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Build::MSYS.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build/Make.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Build::Make.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Build/SearchDep.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Build::SearchDep.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Core.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/CleanInstall.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::CleanInstall.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/Download.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::Download.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/FFI.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::FFI.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/Gather.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::Gather.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/Legacy.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::Legacy.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/Override.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::Override.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/Setup.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::Setup.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Core/Tail.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Core::Tail.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Decode.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Decode.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Decode/DirListing.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Decode::DirListing.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Decode::DirListingFtpcopy.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Decode/HTML.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Decode::HTML.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Decode/Mojo.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Decode::Mojo.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Digest.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Digest.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Digest/Negotiate.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Digest::Negotiate.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Digest/SHA.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Digest::SHA.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Digest/SHAPP.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Digest::SHAPP.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Download.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Download.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Download/Negotiate.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Download::Negotiate.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Extract.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract/ArchiveTar.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Extract::ArchiveTar.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract/ArchiveZip.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Extract::ArchiveZip.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract/CommandLine.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Extract::CommandLine.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract/Directory.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Extract::Directory.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract/File.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Extract::File.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Extract/Negotiate.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Extract::Negotiate.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/CurlCommand.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::CurlCommand.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/HTTPTiny.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::HTTPTiny.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/LWP.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::LWP.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/Local.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::Local.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/LocalDir.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::LocalDir.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/NetFTP.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::NetFTP.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Fetch/Wget.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Fetch::Wget.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Gather.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Gather.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Gather/IsolateDynamic.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Gather::IsolateDynamic.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/PkgConfig.pod $(INST_MAN3DIR)/Alien::Build::Plugin::PkgConfig.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/PkgConfig/CommandLine.pm $(INST_MAN3DIR)/Alien::Build::Plugin::PkgConfig::CommandLine.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm $(INST_MAN3DIR)/Alien::Build::Plugin::PkgConfig::LibPkgConf.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/PkgConfig/MakeStatic.pm $(INST_MAN3DIR)/Alien::Build::Plugin::PkgConfig::MakeStatic.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/PkgConfig/Negotiate.pm $(INST_MAN3DIR)/Alien::Build::Plugin::PkgConfig::Negotiate.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/PkgConfig/PP.pm $(INST_MAN3DIR)/Alien::Build::Plugin::PkgConfig::PP.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Prefer.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Prefer.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Prefer/BadVersion.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Prefer::BadVersion.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Prefer/GoodVersion.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Prefer::GoodVersion.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Prefer/SortVersions.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Prefer::SortVersions.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Probe.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Probe.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Probe/CBuilder.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Probe::CBuilder.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Probe/CommandLine.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Probe::CommandLine.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Probe/Vcpkg.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Probe::Vcpkg.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Test.pod $(INST_MAN3DIR)/Alien::Build::Plugin::Test.$(MAN3EXT) \
	  lib/Alien/Build/Plugin/Test/Mock.pm $(INST_MAN3DIR)/Alien::Build::Plugin::Test::Mock.$(MAN3EXT) \
	  lib/Alien/Build/Temp.pm $(INST_MAN3DIR)/Alien::Build::Temp.$(MAN3EXT) \
	  lib/Alien/Build/Util.pm $(INST_MAN3DIR)/Alien::Build::Util.$(MAN3EXT) \
	  lib/Alien/Build/Version/Basic.pm $(INST_MAN3DIR)/Alien::Build::Version::Basic.$(MAN3EXT) \
	  lib/Alien/Build/rc.pm $(INST_MAN3DIR)/Alien::Build::rc.$(MAN3EXT) \
	  lib/Alien/Role.pm $(INST_MAN3DIR)/Alien::Role.$(MAN3EXT) \
	  lib/Alien/Util.pm $(INST_MAN3DIR)/Alien::Util.$(MAN3EXT) \
	  lib/Test/Alien.pm $(INST_MAN3DIR)/Test::Alien.$(MAN3EXT) \
	  lib/Test/Alien/Build.pm $(INST_MAN3DIR)/Test::Alien::Build.$(MAN3EXT) \
	  lib/Test/Alien/CanCompile.pm $(INST_MAN3DIR)/Test::Alien::CanCompile.$(MAN3EXT) \
	  lib/Test/Alien/CanPlatypus.pm $(INST_MAN3DIR)/Test::Alien::CanPlatypus.$(MAN3EXT) \
	  lib/Test/Alien/Diag.pm $(INST_MAN3DIR)/Test::Alien::Diag.$(MAN3EXT) \
	  lib/Test/Alien/Run.pm $(INST_MAN3DIR)/Test::Alien::Run.$(MAN3EXT) \
	  lib/Test/Alien/Synthetic.pm $(INST_MAN3DIR)/Test::Alien::Synthetic.$(MAN3EXT) \
	  lib/alienfile.pm $(INST_MAN3DIR)/alienfile.$(MAN3EXT) 




# --- MakeMaker processPL section:


# --- MakeMaker installbin section:


# --- MakeMaker subdirs section:

# none

# --- MakeMaker clean_subdirs section:
clean_subdirs :
	$(NOECHO) $(NOOP)


# --- MakeMaker clean section:

# Delete temporary files but do not touch installed files. We don't delete
# the Makefile here so a later make realclean still has a makefile to use.

clean :: clean_subdirs
	- $(RM_F) \
	  $(BASEEXT).bso $(BASEEXT).def \
	  $(BASEEXT).exp $(BASEEXT).x \
	  $(BOOTSTRAP) $(INST_ARCHAUTODIR)/extralibs.all \
	  $(INST_ARCHAUTODIR)/extralibs.ld $(MAKE_APERL_FILE) \
	  *$(LIB_EXT) *$(OBJ_EXT) \
	  *perl.core MYMETA.json \
	  MYMETA.yml blibdirs.ts \
	  core core.*perl.*.? \
	  core.[0-9] core.[0-9][0-9] \
	  core.[0-9][0-9][0-9] core.[0-9][0-9][0-9][0-9] \
	  core.[0-9][0-9][0-9][0-9][0-9] lib$(BASEEXT).def \
	  mon.out perl \
	  perl$(EXE_EXT) perl.exe \
	  perlmain.c pm_to_blib \
	  pm_to_blib.ts so_locations \
	  tmon.out 
	- $(RM_RF) \
	  .tmp blib 
	  $(NOECHO) $(RM_F) $(MAKEFILE_OLD)
	- $(MV) $(FIRST_MAKEFILE) $(MAKEFILE_OLD) $(DEV_NULL)


# --- MakeMaker realclean_subdirs section:
# so clean is forced to complete before realclean_subdirs runs
realclean_subdirs : clean
	$(NOECHO) $(NOOP)


# --- MakeMaker realclean section:
# Delete temporary files (via clean) and also delete dist files
realclean purge :: realclean_subdirs
	- $(RM_F) \
	  $(FIRST_MAKEFILE) $(MAKEFILE_OLD) 
	- $(RM_RF) \
	  $(DISTVNAME) 


# --- MakeMaker metafile section:
metafile : create_distdir
	$(NOECHO) $(ECHO) Generating META.yml
	$(NOECHO) $(ECHO) '---' > META_new.yml
	$(NOECHO) $(ECHO) 'abstract: '\''Build external dependencies for use in CPAN'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'author:' >> META_new.yml
	$(NOECHO) $(ECHO) '  - '\''Graham Ollis <plicease@cpan.org>, Joel Berger <joel.a.berger@gmail.com>'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'build_requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::MakeMaker: '\''6.64'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Test2::API: '\''1.302096'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Test2::V0: '\''0.000121'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'configure_requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::CBuilder: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::MakeMaker: '\''6.64'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::ParseXS: '\''3.30'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Which: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'dynamic_config: 1' >> META_new.yml
	$(NOECHO) $(ECHO) 'generated_by: '\''ExtUtils::MakeMaker version 7.76, CPAN::Meta::Converter version 2.150010'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'license: perl' >> META_new.yml
	$(NOECHO) $(ECHO) 'meta-spec:' >> META_new.yml
	$(NOECHO) $(ECHO) '  url: http://module-build.sourceforge.net/META-spec-v1.4.html' >> META_new.yml
	$(NOECHO) $(ECHO) '  version: '\''1.4'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'name: Alien-Build' >> META_new.yml
	$(NOECHO) $(ECHO) 'no_index:' >> META_new.yml
	$(NOECHO) $(ECHO) '  directory:' >> META_new.yml
	$(NOECHO) $(ECHO) '    - t' >> META_new.yml
	$(NOECHO) $(ECHO) '    - inc' >> META_new.yml
	$(NOECHO) $(ECHO) 'requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  Capture::Tiny: '\''0.17'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Digest::SHA: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::CBuilder: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::MakeMaker: '\''6.64'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::ParseXS: '\''3.30'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  FFI::CheckLib: '\''0.11'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Which: '\''1.10'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::chdir: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  JSON::PP: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  List::Util: '\''1.33'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Path::Tiny: '\''0.077'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Test2::API: '\''1.302096'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Text::ParseWords: '\''3.26'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  parent: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  perl: '\''5.008004'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'version: '\''2.84'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'x_serialization_backend: '\''CPAN::Meta::YAML version 0.020'\''' >> META_new.yml
	-$(NOECHO) $(MV) META_new.yml $(DISTVNAME)/META.yml
	$(NOECHO) $(ECHO) Generating META.json
	$(NOECHO) $(ECHO) '{' > META_new.json
	$(NOECHO) $(ECHO) '   "abstract" : "Build external dependencies for use in CPAN",' >> META_new.json
	$(NOECHO) $(ECHO) '   "author" : [' >> META_new.json
	$(NOECHO) $(ECHO) '      "Graham Ollis <plicease@cpan.org>, Joel Berger <joel.a.berger@gmail.com>"' >> META_new.json
	$(NOECHO) $(ECHO) '   ],' >> META_new.json
	$(NOECHO) $(ECHO) '   "dynamic_config" : 1,' >> META_new.json
	$(NOECHO) $(ECHO) '   "generated_by" : "ExtUtils::MakeMaker version 7.76, CPAN::Meta::Converter version 2.150010",' >> META_new.json
	$(NOECHO) $(ECHO) '   "license" : [' >> META_new.json
	$(NOECHO) $(ECHO) '      "perl_5"' >> META_new.json
	$(NOECHO) $(ECHO) '   ],' >> META_new.json
	$(NOECHO) $(ECHO) '   "meta-spec" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "url" : "http://search.cpan.org/perldoc?CPAN::Meta::Spec",' >> META_new.json
	$(NOECHO) $(ECHO) '      "version" : 2' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "name" : "Alien-Build",' >> META_new.json
	$(NOECHO) $(ECHO) '   "no_index" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "directory" : [' >> META_new.json
	$(NOECHO) $(ECHO) '         "t",' >> META_new.json
	$(NOECHO) $(ECHO) '         "inc"' >> META_new.json
	$(NOECHO) $(ECHO) '      ]' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "prereqs" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "build" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::MakeMaker" : "6.64"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "configure" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::CBuilder" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::MakeMaker" : "6.64",' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::ParseXS" : "3.30",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Which" : "0"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "runtime" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "Capture::Tiny" : "0.17",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Digest::SHA" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::CBuilder" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::MakeMaker" : "6.64",' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::ParseXS" : "3.30",' >> META_new.json
	$(NOECHO) $(ECHO) '            "FFI::CheckLib" : "0.11",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Which" : "1.10",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::chdir" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "JSON::PP" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "List::Util" : "1.33",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Path::Tiny" : "0.077",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Test2::API" : "1.302096",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Text::ParseWords" : "3.26",' >> META_new.json
	$(NOECHO) $(ECHO) '            "parent" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "perl" : "5.008004"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "test" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "Test2::API" : "1.302096",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Test2::V0" : "0.000121"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      }' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "release_status" : "stable",' >> META_new.json
	$(NOECHO) $(ECHO) '   "version" : "2.84",' >> META_new.json
	$(NOECHO) $(ECHO) '   "x_serialization_backend" : "JSON::PP version 4.16"' >> META_new.json
	$(NOECHO) $(ECHO) '}' >> META_new.json
	-$(NOECHO) $(MV) META_new.json $(DISTVNAME)/META.json


# --- MakeMaker signature section:
signature :
	cpansign -s


# --- MakeMaker dist_basics section:
distclean :: realclean distcheck
	$(NOECHO) $(NOOP)

distcheck :
	$(PERLRUN) "-MExtUtils::Manifest=fullcheck" -e fullcheck

skipcheck :
	$(PERLRUN) "-MExtUtils::Manifest=skipcheck" -e skipcheck

manifest :
	$(PERLRUN) "-MExtUtils::Manifest=mkmanifest" -e mkmanifest

veryclean : realclean
	$(RM_F) *~ */*~ *.orig */*.orig *.bak */*.bak *.old */*.old



# --- MakeMaker dist_core section:

dist : $(DIST_DEFAULT) $(FIRST_MAKEFILE)
	$(NOECHO) $(ABSPERLRUN) -l -e 'print '\''Warning: Makefile possibly out of date with $(VERSION_FROM)'\''' \
	  -e '    if -e '\''$(VERSION_FROM)'\'' and -M '\''$(VERSION_FROM)'\'' < -M '\''$(FIRST_MAKEFILE)'\'';' --

tardist : $(DISTVNAME).tar$(SUFFIX)
	$(NOECHO) $(NOOP)

uutardist : $(DISTVNAME).tar$(SUFFIX)
	uuencode $(DISTVNAME).tar$(SUFFIX) $(DISTVNAME).tar$(SUFFIX) > $(DISTVNAME).tar$(SUFFIX)_uu
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).tar$(SUFFIX)_uu'

$(DISTVNAME).tar$(SUFFIX) : distdir
	$(PREOP)
	$(TO_UNIX)
	$(TAR) $(TARFLAGS) $(DISTVNAME).tar $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(COMPRESS) $(DISTVNAME).tar
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).tar$(SUFFIX)'
	$(POSTOP)

zipdist : $(DISTVNAME).zip
	$(NOECHO) $(NOOP)

$(DISTVNAME).zip : distdir
	$(PREOP)
	$(ZIP) $(ZIPFLAGS) $(DISTVNAME).zip $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).zip'
	$(POSTOP)

shdist : distdir
	$(PREOP)
	$(SHAR) $(DISTVNAME) > $(DISTVNAME).shar
	$(RM_RF) $(DISTVNAME)
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).shar'
	$(POSTOP)


# --- MakeMaker distdir section:
create_distdir :
	$(RM_RF) $(DISTVNAME)
	$(PERLRUN) "-MExtUtils::Manifest=manicopy,maniread" \
		-e "manicopy(maniread(),'$(DISTVNAME)', '$(DIST_CP)');"

distdir : create_distdir distmeta 
	$(NOECHO) $(NOOP)



# --- MakeMaker dist_test section:
disttest : distdir
	cd $(DISTVNAME) && $(ABSPERLRUN) Makefile.PL 
	cd $(DISTVNAME) && $(MAKE) $(PASTHRU)
	cd $(DISTVNAME) && $(MAKE) test $(PASTHRU)



# --- MakeMaker dist_ci section:
ci :
	$(ABSPERLRUN) -MExtUtils::Manifest=maniread -e '@all = sort keys %{ maniread() };' \
	  -e 'print(qq{Executing $(CI) @all\n});' \
	  -e 'system(qq{$(CI) @all}) == 0 or die $$!;' \
	  -e 'print(qq{Executing $(RCS_LABEL) ...\n});' \
	  -e 'system(qq{$(RCS_LABEL) @all}) == 0 or die $$!;' --


# --- MakeMaker distmeta section:
distmeta : create_distdir metafile
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'exit unless -e q{META.yml};' \
	  -e 'eval { maniadd({q{META.yml} => q{Module YAML meta-data (added by MakeMaker)}}) }' \
	  -e '    or die "Could not add META.yml to MANIFEST: $${'\''@'\''}"' --
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'exit unless -f q{META.json};' \
	  -e 'eval { maniadd({q{META.json} => q{Module JSON meta-data (added by MakeMaker)}}) }' \
	  -e '    or die "Could not add META.json to MANIFEST: $${'\''@'\''}"' --



# --- MakeMaker distsignature section:
distsignature : distmeta
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'eval { maniadd({q{SIGNATURE} => q{Public-key signature (added by MakeMaker)}}) }' \
	  -e '    or die "Could not add SIGNATURE to MANIFEST: $${'\''@'\''}"' --
	$(NOECHO) cd $(DISTVNAME) && $(TOUCH) SIGNATURE
	cd $(DISTVNAME) && cpansign -s



# --- MakeMaker install section:

install :: pure_install doc_install
	$(NOECHO) $(NOOP)

install_perl :: pure_perl_install doc_perl_install
	$(NOECHO) $(NOOP)

install_site :: pure_site_install doc_site_install
	$(NOECHO) $(NOOP)

install_vendor :: pure_vendor_install doc_vendor_install
	$(NOECHO) $(NOOP)

pure_install :: pure_$(INSTALLDIRS)_install
	$(NOECHO) $(NOOP)

doc_install :: doc_$(INSTALLDIRS)_install
	$(NOECHO) $(NOOP)

pure__install : pure_site_install
	$(NOECHO) $(ECHO) INSTALLDIRS not defined, defaulting to INSTALLDIRS=site

doc__install : doc_site_install
	$(NOECHO) $(ECHO) INSTALLDIRS not defined, defaulting to INSTALLDIRS=site

pure_perl_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read "$(PERL_ARCHLIB)/auto/$(FULLEXT)/.packlist" \
		write "$(DESTINSTALLARCHLIB)/auto/$(FULLEXT)/.packlist" \
		"$(INST_LIB)" "$(DESTINSTALLPRIVLIB)" \
		"$(INST_ARCHLIB)" "$(DESTINSTALLARCHLIB)" \
		"$(INST_BIN)" "$(DESTINSTALLBIN)" \
		"$(INST_SCRIPT)" "$(DESTINSTALLSCRIPT)" \
		"$(INST_MAN1DIR)" "$(DESTINSTALLMAN1DIR)" \
		"$(INST_MAN3DIR)" "$(DESTINSTALLMAN3DIR)"
	$(NOECHO) $(WARN_IF_OLD_PACKLIST) \
		"$(SITEARCHEXP)/auto/$(FULLEXT)"


pure_site_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read "$(SITEARCHEXP)/auto/$(FULLEXT)/.packlist" \
		write "$(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist" \
		"$(INST_LIB)" "$(DESTINSTALLSITELIB)" \
		"$(INST_ARCHLIB)" "$(DESTINSTALLSITEARCH)" \
		"$(INST_BIN)" "$(DESTINSTALLSITEBIN)" \
		"$(INST_SCRIPT)" "$(DESTINSTALLSITESCRIPT)" \
		"$(INST_MAN1DIR)" "$(DESTINSTALLSITEMAN1DIR)" \
		"$(INST_MAN3DIR)" "$(DESTINSTALLSITEMAN3DIR)"
	$(NOECHO) $(WARN_IF_OLD_PACKLIST) \
		"$(PERL_ARCHLIB)/auto/$(FULLEXT)"

pure_vendor_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read "$(VENDORARCHEXP)/auto/$(FULLEXT)/.packlist" \
		write "$(DESTINSTALLVENDORARCH)/auto/$(FULLEXT)/.packlist" \
		"$(INST_LIB)" "$(DESTINSTALLVENDORLIB)" \
		"$(INST_ARCHLIB)" "$(DESTINSTALLVENDORARCH)" \
		"$(INST_BIN)" "$(DESTINSTALLVENDORBIN)" \
		"$(INST_SCRIPT)" "$(DESTINSTALLVENDORSCRIPT)" \
		"$(INST_MAN1DIR)" "$(DESTINSTALLVENDORMAN1DIR)" \
		"$(INST_MAN3DIR)" "$(DESTINSTALLVENDORMAN3DIR)"


doc_perl_install :: all
	$(NOECHO) $(ECHO) Appending installation info to "$(DESTINSTALLARCHLIB)/perllocal.pod"
	-$(NOECHO) $(MKPATH) "$(DESTINSTALLARCHLIB)"
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLPRIVLIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> "$(DESTINSTALLARCHLIB)/perllocal.pod"

doc_site_install :: all
	$(NOECHO) $(ECHO) Appending installation info to "$(DESTINSTALLARCHLIB)/perllocal.pod"
	-$(NOECHO) $(MKPATH) "$(DESTINSTALLARCHLIB)"
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLSITELIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> "$(DESTINSTALLARCHLIB)/perllocal.pod"

doc_vendor_install :: all
	$(NOECHO) $(ECHO) Appending installation info to "$(DESTINSTALLARCHLIB)/perllocal.pod"
	-$(NOECHO) $(MKPATH) "$(DESTINSTALLARCHLIB)"
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLVENDORLIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> "$(DESTINSTALLARCHLIB)/perllocal.pod"


uninstall :: uninstall_from_$(INSTALLDIRS)dirs
	$(NOECHO) $(NOOP)

uninstall_from_perldirs ::
	$(NOECHO) $(UNINSTALL) "$(PERL_ARCHLIB)/auto/$(FULLEXT)/.packlist"

uninstall_from_sitedirs ::
	$(NOECHO) $(UNINSTALL) "$(SITEARCHEXP)/auto/$(FULLEXT)/.packlist"

uninstall_from_vendordirs ::
	$(NOECHO) $(UNINSTALL) "$(VENDORARCHEXP)/auto/$(FULLEXT)/.packlist"


# --- MakeMaker force section:
# Phony target to force checking subdirectories.
FORCE :
	$(NOECHO) $(NOOP)


# --- MakeMaker perldepend section:


# --- MakeMaker makefile section:
# We take a very conservative approach here, but it's worth it.
# We move Makefile to Makefile.old here to avoid gnu make looping.
$(FIRST_MAKEFILE) : Makefile.PL $(CONFIGDEP)
	$(NOECHO) $(ECHO) "Makefile out-of-date with respect to $?"
	$(NOECHO) $(ECHO) "Cleaning current config before rebuilding Makefile..."
	-$(NOECHO) $(RM_F) $(MAKEFILE_OLD)
	-$(NOECHO) $(MV)   $(FIRST_MAKEFILE) $(MAKEFILE_OLD)
	- $(MAKE) $(USEMAKEFILE) $(MAKEFILE_OLD) clean $(DEV_NULL)
	$(PERLRUN) Makefile.PL 
	$(NOECHO) $(ECHO) "==> Your Makefile has been rebuilt. <=="
	$(NOECHO) $(ECHO) "==> Please rerun the $(MAKE) command.  <=="
	$(FALSE)



# --- MakeMaker staticmake section:

# --- MakeMaker makeaperl section ---
MAP_TARGET    = perl
FULLPERL      = "/data/data/com.termux/files/usr/bin/perl"
MAP_PERLINC   = "-Iblib/arch" "-Iblib/lib" "-I/data/data/com.termux/files/usr/lib/perl5/5.42.0/aarch64-android" "-I/data/data/com.termux/files/usr/lib/perl5/5.42.0"

$(MAP_TARGET) :: $(MAKE_APERL_FILE)
	$(MAKE) $(USEMAKEFILE) $(MAKE_APERL_FILE) $@

$(MAKE_APERL_FILE) : static $(FIRST_MAKEFILE) pm_to_blib
	$(NOECHO) $(ECHO) Writing \"$(MAKE_APERL_FILE)\" for this $(MAP_TARGET)
	$(NOECHO) $(PERLRUNINST) \
		Makefile.PL DIR="" \
		MAKEFILE=$(MAKE_APERL_FILE) LINKTYPE=static \
		MAKEAPERL=1 NORECURS=1 CCCDLFLAGS=


# --- MakeMaker test section:
TEST_VERBOSE=0
TEST_TYPE=test_$(LINKTYPE)
TEST_FILE = test.pl
TEST_FILES = t/*.t
TESTDB_SW = -d

testdb :: testdb_$(LINKTYPE)
	$(NOECHO) $(NOOP)

test :: $(TEST_TYPE)
	$(NOECHO) $(NOOP)

# Occasionally we may face this degenerate target:
test_ : test_dynamic
	$(NOECHO) $(NOOP)

subdirs-test_dynamic :: dynamic pure_all

test_dynamic :: subdirs-test_dynamic
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness($(TEST_VERBOSE), '$(INST_LIB)', '$(INST_ARCHLIB)')" $(TEST_FILES)

testdb_dynamic :: dynamic pure_all
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) $(TESTDB_SW) "-I$(INST_LIB)" "-I$(INST_ARCHLIB)" $(TEST_FILE)

subdirs-test_static :: static pure_all

test_static :: subdirs-test_static
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness($(TEST_VERBOSE), '$(INST_LIB)', '$(INST_ARCHLIB)')" $(TEST_FILES)

testdb_static :: static pure_all
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) $(TESTDB_SW) "-I$(INST_LIB)" "-I$(INST_ARCHLIB)" $(TEST_FILE)



# --- MakeMaker ppd section:
# Creates a PPD (Perl Package Description) for a binary distribution.
ppd :
	$(NOECHO) $(ECHO) '<SOFTPKG NAME="Alien-Build" VERSION="2.84">' > Alien-Build.ppd
	$(NOECHO) $(ECHO) '    <ABSTRACT>Build external dependencies for use in CPAN</ABSTRACT>' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '    <AUTHOR>Graham Ollis &lt;plicease@cpan.org&gt;, Joel Berger &lt;joel.a.berger@gmail.com&gt;</AUTHOR>' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '    <IMPLEMENTATION>' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <PERLCORE VERSION="5,008004,0,0" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Capture::Tiny" VERSION="0.17" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Digest::SHA" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="ExtUtils::CBuilder" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="ExtUtils::MakeMaker" VERSION="6.64" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="ExtUtils::ParseXS" VERSION="3.30" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="FFI::CheckLib" VERSION="0.11" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::Which" VERSION="1.10" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::chdir" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="JSON::PP" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="List::Util" VERSION="1.33" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Path::Tiny" VERSION="0.077" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Test2::API" VERSION="1.302096" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Text::ParseWords" VERSION="3.26" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="parent::" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <ARCHITECTURE NAME="aarch64-android-5.42" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '        <CODEBASE HREF="" />' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '    </IMPLEMENTATION>' >> Alien-Build.ppd
	$(NOECHO) $(ECHO) '</SOFTPKG>' >> Alien-Build.ppd


# --- MakeMaker pm_to_blib section:

pm_to_blib : $(FIRST_MAKEFILE) $(TO_INST_PM)
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e '$$i=0; $$n=$$#ARGV; $$i++ until $$i > $$n or $$ARGV[$$i] eq q{--};' \
	  -e 'die q{Failed to find -- in }.join(q{|},@ARGV) if $$i > $$n;' \
	  -e '@parts=splice @ARGV,0,$$i+1;' \
	  -e 'pop @parts; $$filter=join q{ }, map qq{"$$_"}, @parts;' \
	  -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', $$filter, '\''$(PERM_DIR)'\'')' -- $(PM_FILTER) -- \
	  'lib/Alien/Base.pm' '$(INST_LIB)/Alien/Base.pm' \
	  'lib/Alien/Base/Authoring.pod' '$(INST_LIB)/Alien/Base/Authoring.pod' \
	  'lib/Alien/Base/FAQ.pod' '$(INST_LIB)/Alien/Base/FAQ.pod' \
	  'lib/Alien/Base/PkgConfig.pm' '$(INST_LIB)/Alien/Base/PkgConfig.pm' \
	  'lib/Alien/Base/Wrapper.pm' '$(INST_LIB)/Alien/Base/Wrapper.pm' \
	  'lib/Alien/Build.pm' '$(INST_LIB)/Alien/Build.pm' \
	  'lib/Alien/Build/CommandSequence.pm' '$(INST_LIB)/Alien/Build/CommandSequence.pm' \
	  'lib/Alien/Build/Interpolate.pm' '$(INST_LIB)/Alien/Build/Interpolate.pm' \
	  'lib/Alien/Build/Interpolate/Default.pm' '$(INST_LIB)/Alien/Build/Interpolate/Default.pm' \
	  'lib/Alien/Build/Log.pm' '$(INST_LIB)/Alien/Build/Log.pm' \
	  'lib/Alien/Build/Log/Abbreviate.pm' '$(INST_LIB)/Alien/Build/Log/Abbreviate.pm' \
	  'lib/Alien/Build/Log/Default.pm' '$(INST_LIB)/Alien/Build/Log/Default.pm' \
	  'lib/Alien/Build/MM.pm' '$(INST_LIB)/Alien/Build/MM.pm' \
	  'lib/Alien/Build/Manual.pod' '$(INST_LIB)/Alien/Build/Manual.pod' \
	  'lib/Alien/Build/Manual/Alien.pod' '$(INST_LIB)/Alien/Build/Manual/Alien.pod' \
	  'lib/Alien/Build/Manual/AlienAuthor.pod' '$(INST_LIB)/Alien/Build/Manual/AlienAuthor.pod' \
	  'lib/Alien/Build/Manual/AlienUser.pod' '$(INST_LIB)/Alien/Build/Manual/AlienUser.pod' \
	  'lib/Alien/Build/Manual/Contributing.pod' '$(INST_LIB)/Alien/Build/Manual/Contributing.pod' \
	  'lib/Alien/Build/Manual/FAQ.pod' '$(INST_LIB)/Alien/Build/Manual/FAQ.pod' \
	  'lib/Alien/Build/Manual/PluginAuthor.pod' '$(INST_LIB)/Alien/Build/Manual/PluginAuthor.pod' \
	  'lib/Alien/Build/Manual/Security.pod' '$(INST_LIB)/Alien/Build/Manual/Security.pod' \
	  'lib/Alien/Build/Plugin.pm' '$(INST_LIB)/Alien/Build/Plugin.pm' \
	  'lib/Alien/Build/Plugin/Build.pod' '$(INST_LIB)/Alien/Build/Plugin/Build.pod' \
	  'lib/Alien/Build/Plugin/Build/Autoconf.pm' '$(INST_LIB)/Alien/Build/Plugin/Build/Autoconf.pm' \
	  'lib/Alien/Build/Plugin/Build/CMake.pm' '$(INST_LIB)/Alien/Build/Plugin/Build/CMake.pm' \
	  'lib/Alien/Build/Plugin/Build/Copy.pm' '$(INST_LIB)/Alien/Build/Plugin/Build/Copy.pm' \
	  'lib/Alien/Build/Plugin/Build/MSYS.pm' '$(INST_LIB)/Alien/Build/Plugin/Build/MSYS.pm' \
	  'lib/Alien/Build/Plugin/Build/Make.pm' '$(INST_LIB)/Alien/Build/Plugin/Build/Make.pm' \
	  'lib/Alien/Build/Plugin/Build/SearchDep.pm' '$(INST_LIB)/Alien/Build/Plugin/Build/SearchDep.pm' \
	  'lib/Alien/Build/Plugin/Core.pod' '$(INST_LIB)/Alien/Build/Plugin/Core.pod' \
	  'lib/Alien/Build/Plugin/Core/CleanInstall.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/CleanInstall.pm' \
	  'lib/Alien/Build/Plugin/Core/Download.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/Download.pm' \
	  'lib/Alien/Build/Plugin/Core/FFI.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/FFI.pm' \
	  'lib/Alien/Build/Plugin/Core/Gather.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/Gather.pm' \
	  'lib/Alien/Build/Plugin/Core/Legacy.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/Legacy.pm' \
	  'lib/Alien/Build/Plugin/Core/Override.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/Override.pm' \
	  'lib/Alien/Build/Plugin/Core/Setup.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/Setup.pm' \
	  'lib/Alien/Build/Plugin/Core/Tail.pm' '$(INST_LIB)/Alien/Build/Plugin/Core/Tail.pm' \
	  'lib/Alien/Build/Plugin/Decode.pod' '$(INST_LIB)/Alien/Build/Plugin/Decode.pod' \
	  'lib/Alien/Build/Plugin/Decode/DirListing.pm' '$(INST_LIB)/Alien/Build/Plugin/Decode/DirListing.pm' \
	  'lib/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm' '$(INST_LIB)/Alien/Build/Plugin/Decode/DirListingFtpcopy.pm' \
	  'lib/Alien/Build/Plugin/Decode/HTML.pm' '$(INST_LIB)/Alien/Build/Plugin/Decode/HTML.pm' \
	  'lib/Alien/Build/Plugin/Decode/Mojo.pm' '$(INST_LIB)/Alien/Build/Plugin/Decode/Mojo.pm' \
	  'lib/Alien/Build/Plugin/Digest.pod' '$(INST_LIB)/Alien/Build/Plugin/Digest.pod' \
	  'lib/Alien/Build/Plugin/Digest/Negotiate.pm' '$(INST_LIB)/Alien/Build/Plugin/Digest/Negotiate.pm' \
	  'lib/Alien/Build/Plugin/Digest/SHA.pm' '$(INST_LIB)/Alien/Build/Plugin/Digest/SHA.pm' \
	  'lib/Alien/Build/Plugin/Digest/SHAPP.pm' '$(INST_LIB)/Alien/Build/Plugin/Digest/SHAPP.pm' \
	  'lib/Alien/Build/Plugin/Download.pod' '$(INST_LIB)/Alien/Build/Plugin/Download.pod' \
	  'lib/Alien/Build/Plugin/Download/Negotiate.pm' '$(INST_LIB)/Alien/Build/Plugin/Download/Negotiate.pm' \
	  'lib/Alien/Build/Plugin/Extract.pod' '$(INST_LIB)/Alien/Build/Plugin/Extract.pod' \
	  'lib/Alien/Build/Plugin/Extract/ArchiveTar.pm' '$(INST_LIB)/Alien/Build/Plugin/Extract/ArchiveTar.pm' \
	  'lib/Alien/Build/Plugin/Extract/ArchiveZip.pm' '$(INST_LIB)/Alien/Build/Plugin/Extract/ArchiveZip.pm' \
	  'lib/Alien/Build/Plugin/Extract/CommandLine.pm' '$(INST_LIB)/Alien/Build/Plugin/Extract/CommandLine.pm' \
	  'lib/Alien/Build/Plugin/Extract/Directory.pm' '$(INST_LIB)/Alien/Build/Plugin/Extract/Directory.pm' \
	  'lib/Alien/Build/Plugin/Extract/File.pm' '$(INST_LIB)/Alien/Build/Plugin/Extract/File.pm' \
	  'lib/Alien/Build/Plugin/Extract/Negotiate.pm' '$(INST_LIB)/Alien/Build/Plugin/Extract/Negotiate.pm' \
	  'lib/Alien/Build/Plugin/Fetch.pod' '$(INST_LIB)/Alien/Build/Plugin/Fetch.pod' \
	  'lib/Alien/Build/Plugin/Fetch/CurlCommand.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/CurlCommand.pm' \
	  'lib/Alien/Build/Plugin/Fetch/HTTPTiny.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/HTTPTiny.pm' \
	  'lib/Alien/Build/Plugin/Fetch/LWP.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/LWP.pm' \
	  'lib/Alien/Build/Plugin/Fetch/Local.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/Local.pm' \
	  'lib/Alien/Build/Plugin/Fetch/LocalDir.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/LocalDir.pm' \
	  'lib/Alien/Build/Plugin/Fetch/NetFTP.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/NetFTP.pm' \
	  'lib/Alien/Build/Plugin/Fetch/Wget.pm' '$(INST_LIB)/Alien/Build/Plugin/Fetch/Wget.pm' \
	  'lib/Alien/Build/Plugin/Gather.pod' '$(INST_LIB)/Alien/Build/Plugin/Gather.pod' \
	  'lib/Alien/Build/Plugin/Gather/IsolateDynamic.pm' '$(INST_LIB)/Alien/Build/Plugin/Gather/IsolateDynamic.pm' \
	  'lib/Alien/Build/Plugin/PkgConfig.pod' '$(INST_LIB)/Alien/Build/Plugin/PkgConfig.pod' \
	  'lib/Alien/Build/Plugin/PkgConfig/CommandLine.pm' '$(INST_LIB)/Alien/Build/Plugin/PkgConfig/CommandLine.pm' \
	  'lib/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm' '$(INST_LIB)/Alien/Build/Plugin/PkgConfig/LibPkgConf.pm' \
	  'lib/Alien/Build/Plugin/PkgConfig/MakeStatic.pm' '$(INST_LIB)/Alien/Build/Plugin/PkgConfig/MakeStatic.pm' \
	  'lib/Alien/Build/Plugin/PkgConfig/Negotiate.pm' '$(INST_LIB)/Alien/Build/Plugin/PkgConfig/Negotiate.pm' \
	  'lib/Alien/Build/Plugin/PkgConfig/PP.pm' '$(INST_LIB)/Alien/Build/Plugin/PkgConfig/PP.pm' \
	  'lib/Alien/Build/Plugin/Prefer.pod' '$(INST_LIB)/Alien/Build/Plugin/Prefer.pod' \
	  'lib/Alien/Build/Plugin/Prefer/BadVersion.pm' '$(INST_LIB)/Alien/Build/Plugin/Prefer/BadVersion.pm' \
	  'lib/Alien/Build/Plugin/Prefer/GoodVersion.pm' '$(INST_LIB)/Alien/Build/Plugin/Prefer/GoodVersion.pm' \
	  'lib/Alien/Build/Plugin/Prefer/SortVersions.pm' '$(INST_LIB)/Alien/Build/Plugin/Prefer/SortVersions.pm' \
	  'lib/Alien/Build/Plugin/Probe.pod' '$(INST_LIB)/Alien/Build/Plugin/Probe.pod' \
	  'lib/Alien/Build/Plugin/Probe/CBuilder.pm' '$(INST_LIB)/Alien/Build/Plugin/Probe/CBuilder.pm' \
	  'lib/Alien/Build/Plugin/Probe/CommandLine.pm' '$(INST_LIB)/Alien/Build/Plugin/Probe/CommandLine.pm' \
	  'lib/Alien/Build/Plugin/Probe/Vcpkg.pm' '$(INST_LIB)/Alien/Build/Plugin/Probe/Vcpkg.pm' \
	  'lib/Alien/Build/Plugin/Test.pod' '$(INST_LIB)/Alien/Build/Plugin/Test.pod' \
	  'lib/Alien/Build/Plugin/Test/Mock.pm' '$(INST_LIB)/Alien/Build/Plugin/Test/Mock.pm' \
	  'lib/Alien/Build/Temp.pm' '$(INST_LIB)/Alien/Build/Temp.pm' \
	  'lib/Alien/Build/Util.pm' '$(INST_LIB)/Alien/Build/Util.pm' \
	  'lib/Alien/Build/Version/Basic.pm' '$(INST_LIB)/Alien/Build/Version/Basic.pm' \
	  'lib/Alien/Build/rc.pm' '$(INST_LIB)/Alien/Build/rc.pm' \
	  'lib/Alien/Role.pm' '$(INST_LIB)/Alien/Role.pm' \
	  'lib/Alien/Util.pm' '$(INST_LIB)/Alien/Util.pm' \
	  'lib/Test/Alien.pm' '$(INST_LIB)/Test/Alien.pm' \
	  'lib/Test/Alien/Build.pm' '$(INST_LIB)/Test/Alien/Build.pm' \
	  'lib/Test/Alien/CanCompile.pm' '$(INST_LIB)/Test/Alien/CanCompile.pm' \
	  'lib/Test/Alien/CanPlatypus.pm' '$(INST_LIB)/Test/Alien/CanPlatypus.pm' \
	  'lib/Test/Alien/Diag.pm' '$(INST_LIB)/Test/Alien/Diag.pm' \
	  'lib/Test/Alien/Run.pm' '$(INST_LIB)/Test/Alien/Run.pm' \
	  'lib/Test/Alien/Synthetic.pm' '$(INST_LIB)/Test/Alien/Synthetic.pm' \
	  'lib/alienfile.pm' '$(INST_LIB)/alienfile.pm' 
	$(NOECHO) $(TOUCH) pm_to_blib


# --- MakeMaker selfdocument section:

# here so even if top_targets is overridden, these will still be defined
# gmake will silently still work if any are .PHONY-ed but nmake won't

test_static ::
	$(NOECHO) $(NOOP)

test_dynamic ::
	$(NOECHO) $(NOOP)

static ::
	$(NOECHO) $(NOOP)

dynamic ::
	$(NOECHO) $(NOOP)

config ::
	$(NOECHO) $(NOOP)


# --- MakeMaker postamble section:


# End.
