#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mm-common
Version  : 1.0.1
Release  : 4
URL      : file:///insilications/build/clearlinux/packages/mm-common/mm-common-1.0.1.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/mm-common/mm-common-1.0.1.tar.gz
Summary  : mm-common's doctool build utilities for the GNOME C++ bindings
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: mm-common-bin = %{version}-%{release}
Requires: mm-common-data = %{version}-%{release}
Requires: mm-common-man = %{version}-%{release}
BuildRequires : atkmm-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : findutils
BuildRequires : gtk+-dev
BuildRequires : gtkmm2-dev
BuildRequires : gtkmm3-dev
BuildRequires : libstdc++-dev
BuildRequires : pangomm-dev
BuildRequires : pkgconfig(atkmm-1.6)
BuildRequires : pkgconfig(cairomm-1.0)
BuildRequires : pkgconfig(giomm-2.4)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(pangomm-1.4)
BuildRequires : python3
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This module is part of the GNOME C++ bindings effort <http://www.gtkmm.org/>.
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is only a required
dependency for building the C++ bindings from the gnome.org version
control repository.  An installation of mm-common is not required for
building tarball releases, unless configured to use maintainer-mode.

%package bin
Summary: bin components for the mm-common package.
Group: Binaries
Requires: mm-common-data = %{version}-%{release}

%description bin
bin components for the mm-common package.


%package data
Summary: data components for the mm-common package.
Group: Data

%description data
data components for the mm-common package.


%package dev
Summary: dev components for the mm-common package.
Group: Development
Requires: mm-common-bin = %{version}-%{release}
Requires: mm-common-data = %{version}-%{release}
Provides: mm-common-devel = %{version}-%{release}
Requires: mm-common = %{version}-%{release}

%description dev
dev components for the mm-common package.


%package doc
Summary: doc components for the mm-common package.
Group: Documentation
Requires: mm-common-man = %{version}-%{release}

%description doc
doc components for the mm-common package.


%package man
Summary: man components for the mm-common package.
Group: Default

%description man
man components for the mm-common package.


%prep
%setup -q -n mm-common
cd %{_builddir}/mm-common

%build
## build_prepend content
unset http_proxy
unset https_proxy
unset no_proxy
unset ftp_proxy
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599712292
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
# -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Duse-network=true  builddir
## make_prepend content
unset http_proxy
unset https_proxy
unset no_proxy
unset ftp_proxy
## make_prepend end
ninja -v -C builddir

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
meson test -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mm-common-get
/usr/bin/mm-common-prepare

%files data
%defattr(-,root,root,-)
/usr/share/mm-common/build/check-dllexport-usage.py
/usr/share/mm-common/build/compile-binding.am
/usr/share/mm-common/build/dist-build-scripts.py
/usr/share/mm-common/build/dist-changelog.am
/usr/share/mm-common/build/dist-changelog.py
/usr/share/mm-common/build/doc-reference.am
/usr/share/mm-common/build/doc-reference.py
/usr/share/mm-common/build/generate-binding.am
/usr/share/mm-common/build/generate-binding.py
/usr/share/mm-common/doctags/libstdc++.tag
/usr/share/mm-common/doctool/doc-install.pl
/usr/share/mm-common/doctool/doc-postprocess.pl
/usr/share/mm-common/doctool/doxygen-extra.css
/usr/share/mm-common/doctool/doxygen.css
/usr/share/mm-common/doctool/tagfile-to-devhelp2.xsl
/usr/share/pkgconfig/mm-common-libstdc++.pc
/usr/share/pkgconfig/mm-common-util.pc

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/mm\-common/*

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mm-common-get.1
/usr/share/man/man1/mm-common-prepare.1
