#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : syntax-highlighting
Version  : 5.115.0
Release  : 75
URL      : https://download.kde.org/stable/frameworks/5.115/syntax-highlighting-5.115.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.115/syntax-highlighting-5.115.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.115/syntax-highlighting-5.115.0.tar.xz.sig
Summary  : Recorder for internet radios (based on Streamripper)
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 MIT
Requires: syntax-highlighting-bin = %{version}-%{release}
Requires: syntax-highlighting-data = %{version}-%{release}
Requires: syntax-highlighting-lib = %{version}-%{release}
Requires: syntax-highlighting-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : perl
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Syntax Highlighting
Syntax highlighting engine for Kate syntax definitions
## Table of contents

%package bin
Summary: bin components for the syntax-highlighting package.
Group: Binaries
Requires: syntax-highlighting-data = %{version}-%{release}
Requires: syntax-highlighting-license = %{version}-%{release}

%description bin
bin components for the syntax-highlighting package.


%package data
Summary: data components for the syntax-highlighting package.
Group: Data

%description data
data components for the syntax-highlighting package.


%package dev
Summary: dev components for the syntax-highlighting package.
Group: Development
Requires: syntax-highlighting-lib = %{version}-%{release}
Requires: syntax-highlighting-bin = %{version}-%{release}
Requires: syntax-highlighting-data = %{version}-%{release}
Provides: syntax-highlighting-devel = %{version}-%{release}
Requires: syntax-highlighting = %{version}-%{release}

%description dev
dev components for the syntax-highlighting package.


%package lib
Summary: lib components for the syntax-highlighting package.
Group: Libraries
Requires: syntax-highlighting-data = %{version}-%{release}
Requires: syntax-highlighting-license = %{version}-%{release}

%description lib
lib components for the syntax-highlighting package.


%package license
Summary: license components for the syntax-highlighting package.
Group: Default

%description license
license components for the syntax-highlighting package.


%prep
%setup -q -n syntax-highlighting-5.115.0
cd %{_builddir}/syntax-highlighting-5.115.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707695724
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-apx
pushd clr-build-apx
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CC=gcc-14
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707695724
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/syntax-highlighting
cp %{_builddir}/syntax-highlighting-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/syntax-highlighting/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/syntax-highlighting-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/syntax-highlighting/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/syntax-highlighting-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/syntax-highlighting/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/syntax-highlighting-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/syntax-highlighting/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/syntax-highlighting-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/syntax-highlighting/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/syntax-highlighting-%{version}/docs/qml-api.md.license %{buildroot}/usr/share/package-licenses/syntax-highlighting/28ba3ebe1aa04fad742c69eb685e2a5376e9276f || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v3
pushd clr-build-apx
%make_install_va  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kate-syntax-highlighter
/usr/bin/kate-syntax-highlighter

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/az/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/be/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/br/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/da/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/de/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/el/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/es/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/et/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/he/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/id/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/is/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/it/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/km/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/se/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/si/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/th/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/qlogging-categories5/ksyntaxhighlighting.categories
/usr/share/qlogging-categories5/ksyntaxhighlighting.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/AbstractHighlighter
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/Definition
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/DefinitionDownloader
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/FoldingRegion
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/Format
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/Repository
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/State
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/SyntaxHighlighter
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/Theme
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/WildcardMatcher
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/abstracthighlighter.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/definition.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/definitiondownloader.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/foldingregion.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/format.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/ksyntaxhighlighting_export.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/repository.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/state.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/syntaxhighlighter.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/theme.h
/usr/include/KF5/KSyntaxHighlighting/KSyntaxHighlighting/wildcardmatcher.h
/usr/include/KF5/KSyntaxHighlighting/ksyntaxhighlighting_version.h
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingConfig.cmake
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingConfigVersion.cmake
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingTargets.cmake
/usr/lib64/libKF5SyntaxHighlighting.so
/usr/lib64/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5SyntaxHighlighting.so.5.115.0
/V3/usr/lib64/qt5/qml/org/kde/syntaxhighlighting/libkquicksyntaxhighlightingplugin.so
/usr/lib64/libKF5SyntaxHighlighting.so.5
/usr/lib64/libKF5SyntaxHighlighting.so.5.115.0
/usr/lib64/qt5/qml/org/kde/syntaxhighlighting/libkquicksyntaxhighlightingplugin.so
/usr/lib64/qt5/qml/org/kde/syntaxhighlighting/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/syntax-highlighting/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/syntax-highlighting/28ba3ebe1aa04fad742c69eb685e2a5376e9276f
/usr/share/package-licenses/syntax-highlighting/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/syntax-highlighting/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/syntax-highlighting/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/syntax-highlighting/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
