#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mm-common
Version  : 1
Release  : 2
URL      : https://github.com/GNOME/mm-common/archive/mainline.zip
Source0  : https://github.com/GNOME/mm-common/archive/mainline.zip
Summary  : mm-common's doctool build utilities for the GNOME C++ bindings
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: mm-common-bin = %{version}-%{release}
Requires: mm-common-data = %{version}-%{release}
Requires: mm-common-man = %{version}-%{release}
BuildRequires : atkmm-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
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
%setup -q -n mm-common-mainline
cd %{_builddir}/mm-common-mainline

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
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587079189
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FCFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export CFFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export LDFLAGS="-O3 -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native "
export CXXFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
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
