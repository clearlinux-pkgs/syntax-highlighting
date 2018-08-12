#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : syntax-highlighting
Version  : 5.49.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.49/syntax-highlighting-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/syntax-highlighting-5.49.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.49/syntax-highlighting-5.49.0.tar.xz.sig
Summary  : Recorder for internet radios (based on Streamripper)
Group    : Development/Tools
License  : LGPL-2.1
Requires: syntax-highlighting-bin
Requires: syntax-highlighting-lib
Requires: syntax-highlighting-license
Requires: syntax-highlighting-data
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-meson
BuildRequires : perl
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
# Syntax Highlighting
Syntax highlighting engine for Kate syntax definitions
## Introduction

%package bin
Summary: bin components for the syntax-highlighting package.
Group: Binaries
Requires: syntax-highlighting-data
Requires: syntax-highlighting-license

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
Requires: syntax-highlighting-lib
Requires: syntax-highlighting-bin
Requires: syntax-highlighting-data
Provides: syntax-highlighting-devel

%description dev
dev components for the syntax-highlighting package.


%package lib
Summary: lib components for the syntax-highlighting package.
Group: Libraries
Requires: syntax-highlighting-data
Requires: syntax-highlighting-license

%description lib
lib components for the syntax-highlighting package.


%package license
Summary: license components for the syntax-highlighting package.
Group: Default

%description license
license components for the syntax-highlighting package.


%prep
%setup -q -n syntax-highlighting-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534106670
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1534106670
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/syntax-highlighting
cp COPYING.LIB %{buildroot}/usr/share/doc/syntax-highlighting/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kate-syntax-highlighter

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/syntaxhighlighting5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/syntaxhighlighting5_qt.qm
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

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KSyntaxHighlighting/AbstractHighlighter
/usr/include/KF5/KSyntaxHighlighting/Definition
/usr/include/KF5/KSyntaxHighlighting/FoldingRegion
/usr/include/KF5/KSyntaxHighlighting/Format
/usr/include/KF5/KSyntaxHighlighting/Repository
/usr/include/KF5/KSyntaxHighlighting/State
/usr/include/KF5/KSyntaxHighlighting/SyntaxHighlighter
/usr/include/KF5/KSyntaxHighlighting/Theme
/usr/include/KF5/KSyntaxHighlighting/abstracthighlighter.h
/usr/include/KF5/KSyntaxHighlighting/definition.h
/usr/include/KF5/KSyntaxHighlighting/foldingregion.h
/usr/include/KF5/KSyntaxHighlighting/format.h
/usr/include/KF5/KSyntaxHighlighting/ksyntaxhighlighting_export.h
/usr/include/KF5/KSyntaxHighlighting/repository.h
/usr/include/KF5/KSyntaxHighlighting/state.h
/usr/include/KF5/KSyntaxHighlighting/syntaxhighlighter.h
/usr/include/KF5/KSyntaxHighlighting/theme.h
/usr/include/KF5/ksyntaxhighlighting_version.h
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingConfig.cmake
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingConfigVersion.cmake
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5SyntaxHighlighting/KF5SyntaxHighlightingTargets.cmake
/usr/lib64/libKF5SyntaxHighlighting.so
/usr/lib64/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5SyntaxHighlighting.so.5
/usr/lib64/libKF5SyntaxHighlighting.so.5.49.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/syntax-highlighting/COPYING.LIB
