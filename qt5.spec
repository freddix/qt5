%include	/usr/lib/rpm/macros.perl

Summary:	Application and UI framework
Name:		qt5
Version:	5.3.2
Release:	0.3
License:	GPL/QPL
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/single/qt-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	c4e893678e3d8388ab04d059523d1d78
URL:		http://www.qtsoftware.com/
BuildRequires:	Mesa-GLU-devel
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libGLES-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	dbus-devel
BuildRequires:	elfutils-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib4-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+-devel
BuildRequires:	icu-devel
BuildRequires:	libdrm-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	openssl-devel
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRequires:	sqlite3-devel
BuildRequires:	systemd-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-libSM-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-libXtst-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt is a cross-platform application and UI framework for developers
using C++ or QML, a CSS & JavaScript like language.

# qtbase
%package -n Qt5Core
Summary:	Qt5Core library
Group:		Libraries

%description -n Qt5Core
Qt5Core library.

%package -n Qt5Concurrent
Summary:	Qt5Concurrent library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Concurrent
Qt5Concurrent library.

%package -n Qt5DBus
Summary:	Qt5DBus library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5DBus
Qt5DBus library.

%package -n Qt5Network
Summary:	Qt5 library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Network
Qt5Network library.

%package -n Qt5Sql
Summary:	Qt5Sql library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Sql
Qt5Sql library.

%package -n Qt5Test
Summary:	Qt5Test library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Test
Qt5Test library.

%package -n Qt5Xml
Summary:	Qt5Xml library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Xml
Qt5Xml library.

%package -n Qt5Gui
Summary:	Qt5Gui library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Gui
Qt5Gui library.

%package -n Qt5OpenGL
Summary:	Qt5 library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5Widgets = %{version}-%{release}

%description -n Qt5OpenGL
Qt5OpenGL library.

%package -n Qt5PrintSupport
Summary:	Qt5PrintSupport library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5Widgets = %{version}-%{release}

%description -n Qt5PrintSupport
Qt5PrintSupport library.

%package -n Qt5Widgets
Summary:	Qt5Widgets library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Gui = %{version}-%{release}

%description -n Qt5Widgets
Qt5Widgets library.

%package base
Summary:	Qt5 base libraries
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Gui = %{version}-%{release}

%description base
Qt5 base libraries.

%package base-devel
Summary:	Qt5 base - development files
Group:		Development/Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Concurrent = %{version}-%{release}
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5DBus = %{version}-%{release}
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5Network = %{version}-%{release}
Requires:	Qt5OpenGL = %{version}-%{release}
Requires:	Qt5PrintSupport = %{version}-%{release}
Requires:	Qt5Sql = %{version}-%{release}
Requires:	Qt5Test = %{version}-%{release}
Requires:	Qt5Widgets = %{version}-%{release}
Requires:	Qt5Xml = %{version}-%{release}
Requires:	Mesa-libEGL-devel
Requires:	Mesa-libGL-devel
Requires:	dbus-devel
Requires:	glib-devel
Requires:	harfbuzz-devel
Requires:	icu-devel
Requires:	libpng-devel
Requires:	mtdev-devel
Requires:	pcre-devel
Requires:	systemd-devel
Requires:	udev-devel
Requires:	freetype-devel
Requires:	fontconfig-devel
Requires:	xorg-libXrender-devel
Requires:	xorg-libX11-devel
Requires:	xorg-libXext-devel

%description base-devel
Qt5 base - development files.

# qtconectivity
%package -n Qt5Bluetooth
Summary:	Qt5Bluetooth library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Bluetooth
Qt5Bluetooth library.

%package -n Qt5Nfc
Summary:	Qt5Nfc library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Nfc
Qt5Nfc library.

%package declarative-bluetooth
Summary:	Qt5 connectivity - Bluetooth Qml module
Group:		Libraries
Requires:	Qt5Bluetooth = %{version}-%{release}
Requires:	Qt5Qml = %{version}-%{release}

%description declarative-bluetooth
Qt5 connectivity - Bluetooth Qml module.

%package declarative-nfc
Summary:	Qt5 connectivity - Nfc Qml module
Group:		Libraries
Requires:	Qt5Nfc = %{version}-%{release}
Requires:	Qt5Qml = %{version}-%{release}

%description declarative-nfc
Qt5 connectivity - Nfc Qml module.

%package connectivity-devel
Summary:	Qt5 connectivity - development files
Group:		Development/Libraries
Requires:	%{name}-base-devel = %{version}-%{release}

%description connectivity-devel
Qt5 connectivity - development files.

# qtdeclarative
%package -n Qt5Quick
Summary:	Qt5Quick library
Group:		X11/Libraries
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5Qml = %{version}-%{release}
Requires:	Qt5Test = %{version}-%{release}

%description -n Qt5Quick
Qt5Quick library.

%package -n Qt5Qml
Summary:	Qt5Qml library
Group:		X11/Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Network = %{version}-%{release}

%description -n Qt5Qml
Qt5Qml library.

%package declarative
Summary:	Qt5 - qtdeclarative
Group:		X11/Libraries
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5XmlPatterns = %{version}-%{release}

%description declarative
Qt5 - qtdeclarative.

%package declarative-devel
Summary:	Qt5 declarative - development files
Group:		Development/Libraries
Requires:	%{name}-base-devel = %{version}-%{release}

%description declarative-devel
Qt5 declarative - development files.

# qtgraphicaleffects
%package graphicaleffects
Summary:	Qt5 - qtgraphicaleffects
Group:		X11/Libraries
Requires:	Qt5Qml = %{version}-%{release}

%description graphicaleffects
Qt5 - qtgraphicaleffects.

# qtlocation
%package -n Qt5Positioning
Summary:	Qt5Positioning library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Positioning
Qt5Positioning library.

%package location
Summary:	Qt5 location
Group:		Libraries
Requires:	Qt5Positioning = %{version}-%{release}

%description location
Qt5 location.

%package declarative-location
Summary:	Qt5 location - Qml module
Group:		Libraries
Requires:	Qt5Positioning = %{version}-%{release}
Requires:	Qt5Qml = %{version}-%{release}

%description declarative-location
Qt5 location - Qml module.

%package location-devel
Summary:	Qt5 location - development files
Group:		Development/Libraries
Requires:	Qt5Positioning = %{version}-%{release}
Requires:	%{name}-base-devel = %{version}-%{release}

%description location-devel
Qt5 location - development files.

# qtquickcontrols
%package quickcontrols
Summary:	Qt5 - qtquickcontrols
Group:		X11/Libraries
Requires:	Qt5Quick = %{version}-%{release}

%description quickcontrols
Qt5 - qtquickcontrols.

# qtsensors
%package -n Qt5Sensors
Summary:	Qt5Sensors library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5Sensors
Qt5Sensors library.

%package sensors
Summary:	Qt5 - qtsensors
Group:		Libraries
Requires:	Qt5Sensors = %{version}-%{release}

%description sensors
Qt5 - qtsensors.

%package declarative-sensors
Summary:	Qt5Sensors - Qml module
Group:		Libraries
Requires:	Qt5Sensors = %{version}-%{release}
Requires:	Qt5Qml = %{version}-%{release}

%description declarative-sensors
Qt5Sensors - Qml module.

%package sensors-devel
Summary:	Qt5 Sensors - development files
Group:		Development/Libraries
Requires:	Qt5Sensors = %{version}-%{release}
Requires:	%{name}-base-devel = %{version}-%{release}

%description sensors-devel
Qt5 Sensors - development files.

# qtsvg
%package -n Qt5Svg
Summary:	Qt5Svg library
Group:		Libraries
Requires:	Qt5Widgets = %{version}-%{release}

%description -n Qt5Svg
Qt5Svg library.

%package svg-devel
Summary:	Qt5 Svg - development files
Group:		Development/Libraries
Requires:	Qt5Svg = %{version}-%{release}
Requires:	%{name}-base-devel = %{version}-%{release}

%description svg-devel
Qt5 Svg - development files.

# qttools
%package -n Qt5Designer
Summary:	Qt5Designer library
Group:		X11/Libraries
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5Xml = %{version}-%{release}

%description -n Qt5Designer
Qt5Designer library.

%package -n Qt5Help
Summary:	Qt5Help library
Group:		X11/Libraries
Requires:	Qt5CLucene = %{version}-%{release}
Requires:	Qt5Gui = %{version}-%{release}
Requires:	Qt5Network = %{version}-%{release}
Requires:	Qt5Sql = %{version}-%{release}

%description -n Qt5Help
Qt5Help library.

%package -n Qt5CLucene
Summary:	Qt5CLucene library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}

%description -n Qt5CLucene
Qt5CLucene library.

%package tools
Summary:	Qt5 tools
Group:		Applications

%description tools
Qt5 tools.

%package tools-assistant
Summary:	Qt5 tools - Assistant
Group:		X11/Applications

%description tools-assistant
Qt5 tools - Assistant.

%package tools-designer
Summary:	Qt5 tools - Designer
Group:		X11/Applications

%description tools-designer
Qt5 tools - Designer.

%package tools-help
Summary:	Qt5 tools - help
Group:		X11/Applications

%description tools-help
Qt5 tools - help.

%package tools-linguist
Summary:	Qt5 tools - Linguist
Group:		X11/Applications

%description tools-linguist
Qt5 tools - Linguist.

%package tools-qdbus
Summary:	Qt5 tools - qdbus
Group:		X11/Applications

%description tools-qdbus
Qt5 tools - qdbus.

%package tools-devel
Summary:	Qt5 tools - development files
Group:		Development/Libraries
Requires:	%{name}-base-devel = %{version}-%{release}

%description tools-devel
Qt5 tools - development files.

# qtwebkit
%package -n Qt5WebKit
Summary:	Qt5WebKit library
Group:		X11/Libraries
Requires:	Qt5Network = %{version}-%{release}
Requires:	Qt5OpenGL = %{version}-%{release}
Requires:	Qt5Positioning = %{version}-%{release}
Requires:	Qt5PrintSupport = %{version}-%{release}
Requires:	Qt5Quick = %{version}-%{release}
Requires:	Qt5Sql = %{version}-%{release}

%description -n Qt5WebKit
Qt5WebKit library.

%package webkit
Summary:	Qt5 webkit
Group:		X11/Libraries

%description webkit
Qt5 webkit.

%package declarative-webkit
Summary:	Qt5 webkit - Qml module
Group:		Libraries
Requires:	Qt5Webkit = %{version}-%{release}
Requires:	Qt5Qml = %{version}-%{release}

%description declarative-webkit
Qt5 webkit - Qml module.


%package webkit-devel
Summary:	Qt5 webkit - development files
Group:		Development/Libraries
Requires:	%{name}-base-devel = %{version}-%{release}

%description webkit-devel
Qt5 webkit - development files.

# qtxmlpatterns
%package -n Qt5XmlPatterns
Summary:	QtXmlPatterns library
Group:		Libraries
Requires:	Qt5Core = %{version}-%{release}
Requires:	Qt5Network = %{version}-%{release}

%description -n Qt5XmlPatterns
QtXmlPatterns library.

%package xmlpatterns-devel
Summary:	Qt5 xmlpatterns - development files
Group:		Development/Libraries
Requires:	Qt5XmlPatterns = %{version}-%{release}
Requires:	%{name}-base-devel = %{version}-%{release}

%description xmlpatterns-devel
Qt5 xmlpatterns - development files.

%package doc
Summary:	Qt5 documentation
Group:		Documentation

%description doc
Qt5 documentation.

%prep
%setup -qn qt-everywhere-opensource-src-%{version}

# adapt QMAKE FLAGS
%{__sed} -i -e '
	s|QMAKE_CC.*=.*gcc|QMAKE_CC\t\t= %{__cc}|;
	s|QMAKE_CFLAGS_DEBUG.*|QMAKE_CFLAGS_DEBUG\t+= %{debugcflags}|;
	s|QMAKE_CFLAGS_RELEASE.*|QMAKE_CFLAGS_RELEASE\t+= %{rpmcppflags} %{rpmcflags}|;
	s|QMAKE_CXX.*=.*g++|QMAKE_CXX\t\t= %{__cxx}|;
	s|QMAKE_CXXFLAGS_DEBUG.*|QMAKE_CXXFLAGS_DEBUG\t+= %{debugcflags}|;
	s|QMAKE_CXXFLAGS_RELEASE.*|QMAKE_CXXFLAGS_RELEASE\t+= %{rpmcppflags} %{rpmcxxflags}|;
	s|QMAKE_LFLAGS_RELEASE.*|QMAKE_LFLAGS_RELEASE\t+= %{rpmldflags}|;
	s|QMAKE_LINK.*=.*g++|QMAKE_LINK\t\t= %{__cxx}|;
	s|QMAKE_LINK_SHLIB.*=.*g++|QMAKE_LINK_SHLIB\t= %{__cxx}|;
	' qtbase/mkspecs/common/{g++,gcc}-base.conf

# undefine QMAKE_STRIP
%{__sed} -i -e '
	s|^QMAKE_STRIP.*=.*|QMAKE_STRIP\t\t=|;
	' qtbase/mkspecs/common/linux.conf

%build
export OPTFLAGS="%{rpmcflags}"
export PATH=$PWD/bin:$PATH
COMMONOPT=" \
	-prefix %{_libdir}/qt5			\
	-bindir %{_libdir}/qt5/bin  		\
	-libdir %{_libdir}			\
	-libexecdir %{_libdir}/qt5		\
	-datadir %{_datadir}/qt5		\
	-docdir %{_docdir}/qt5			\
	-archdatadir %{_libdir}/qt5		\
	-headerdir %{_includedir}/qt5		\
	-importdir %{_libdir}/qt5/imports	\
	-plugindir %{_libdir}/qt5/plugins	\
	-sysconfdir %{_sysconfdir}/qt5		\
	-translationdir %{_datadir}/qt5/translations	\
	-no-rpath				\
	-no-compile-examples			\
	-nomake examples			\
	-no-separate-debug-info			\
%ifnarch %{x8664}
	-no-avx					\
	-no-avx2				\
	-no-sse2				\
	-no-sse3				\
	-no-sse4.1				\
	-no-sse4.2				\
	-no-ssse3				\
%endif
	-dbus-linked				\
	-journald				\
	-openssl-linked				\
	-optimized-qmake			\
	-reduce-relocations			\
	-release				\
	-system-freetype			\
	-system-harfbuzz			\
	-system-libjpeg				\
	-system-libpng				\
	-system-pcre				\
	-system-sqlite				\
	-system-xcb				\
	-system-xkbcommon			\
	-system-zlib				\
	-confirm-license			\
	-continue				\
	-opensource				\
	-verbose"

SQL=" \
	-no-sql-ibase		\
	-no-sql-mysql		\
	-no-sql-odbc		\
	-no-sql-psql		\
	-no-sql-sqlite2		\
	-plugin-sql-sqlite"

./configure $COMMONOPT $SQL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for target in \
    qtbase \
    qtconnectivity \
    qtdeclarative \
    qtgraphicaleffects \
    qtimageformats  \
    qtlocation \
    qtquick1 \
    qtquickcontrols \
    qtsensors \
    qtsvg \
    qttools \
    qttranslations \
    qtwebkit \
    qtxmlpatterns;
do
	%{__make} -C $target install INSTALL_ROOT=$RPM_BUILD_ROOT
done

# cleanup
%{__sed} -i -e 's,-L%{_libdir} \?,,g' \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

%{__sed} -i -e '/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/' \
	$RPM_BUILD_ROOT%{_libdir}/*.prl

%{__sed} -i -e 's,QT_NO_TRANSLATION QT_QMAKE_LOCATION.*,QT_NO_TRANSLATION QT_QMAKE_LOCATION=%{_libdir}/qt5/bin/qmake,' \
	$RPM_BUILD_ROOT%{_libdir}/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

cd $RPM_BUILD_ROOT%{_bindir}
for bin in $RPM_BUILD_ROOT%{_libdir}/qt5/bin/*; do
    PROG=`basename $bin`
    ln -s ../%{_lib}/qt5/bin/$PROG $PROG
done
cd -

%{__sed} -i 's|${prefix}/bin/|%{_libdir}/qt5/bin/|g' \
    $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

%find_lang assistant --with-qm --without-mo
%find_lang designer --with-qm --without-mo
%find_lang linguist --with-qm --without-mo
%find_lang qmlviewer --with-qm --without-mo
%find_lang qt --with-qm --without-mo
%find_lang qt_help --with-qm --without-mo
%find_lang qtbase --with-qm --without-mo
%find_lang qtconfig --with-qm --without-mo
%find_lang qtconnectivity --with-qm --without-mo
%find_lang qtdeclarative --with-qm --without-mo
%find_lang qtlocation --with-qm --without-mo
%find_lang qtscript --with-qm --without-mo
%find_lang qtxmlpatterns --with-qm --without-mo

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Bluetooth -p /usr/sbin/ldconfig
%postun -n Qt5Bluetooth -p /usr/sbin/ldconfig
%post	-n Qt5CLucene -p /usr/sbin/ldconfig
%postun -n Qt5CLucene -p /usr/sbin/ldconfig
%post	-n Qt5Concurrent -p /usr/sbin/ldconfig
%postun -n Qt5Concurrent -p /usr/sbin/ldconfig
%post	-n Qt5Core -p /usr/sbin/ldconfig
%postun	-n Qt5Core -p /usr/sbin/ldconfig
%post	-n Qt5DBus -p /usr/sbin/ldconfig
%postun -n Qt5DBus -p /usr/sbin/ldconfig
%post	-n Qt5Designer -p /usr/sbin/ldconfig
%postun -n Qt5Designer -p /usr/sbin/ldconfig
%post	-n Qt5Gui -p /usr/sbin/ldconfig
%postun -n Qt5Gui -p /usr/sbin/ldconfig
%post	-n Qt5Help -p /usr/sbin/ldconfig
%postun -n Qt5Help -p /usr/sbin/ldconfig
%post	-n Qt5Network -p /usr/sbin/ldconfig
%postun -n Qt5Network -p /usr/sbin/ldconfig
%post	-n Qt5Nfc -p /usr/sbin/ldconfig
%postun -n Qt5Nfc -p /usr/sbin/ldconfig
%post	-n Qt5OpenGL -p /usr/sbin/ldconfig
%postun -n Qt5OpenGL -p /usr/sbin/ldconfig
%post	-n Qt5Positioning -p /usr/sbin/ldconfig
%postun -n Qt5Positioning -p /usr/sbin/ldconfig
%post	-n Qt5PrintSupport -p /usr/sbin/ldconfig
%postun -n Qt5PrintSupport -p /usr/sbin/ldconfig
%post	-n Qt5Qml -p /usr/sbin/ldconfig
%postun -n Qt5Qml -p /usr/sbin/ldconfig
%post	-n Qt5Quick -p /usr/sbin/ldconfig
%postun -n Qt5Quick -p /usr/sbin/ldconfig
%post	-n Qt5Sensors -p /usr/sbin/ldconfig
%postun -n Qt5Sensors -p /usr/sbin/ldconfig
%post	-n Qt5Sql -p /usr/sbin/ldconfig
%postun -n Qt5Sql -p /usr/sbin/ldconfig
%post	-n Qt5Svg -p /usr/sbin/ldconfig
%postun -n Qt5Svg -p /usr/sbin/ldconfig
%post	-n Qt5Test -p /usr/sbin/ldconfig
%postun -n Qt5Test -p /usr/sbin/ldconfig
%post	-n Qt5WebKit -p /usr/sbin/ldconfig
%postun -n Qt5WebKit -p /usr/sbin/ldconfig
%post	-n Qt5Widgets -p /usr/sbin/ldconfig
%postun -n Qt5Widgets -p /usr/sbin/ldconfig
%post	-n Qt5Xml -p /usr/sbin/ldconfig
%postun -n Qt5Xml -p /usr/sbin/ldconfig

# qtbase
%files -f qt.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5
%dir %{_libdir}/qt5/plugins
%dir %{_datadir}/qt5

%files -n Qt5Core
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Core.so.5
%attr(755,root,root) %{_libdir}/libQt5Core.so.*.*.*

%files -n Qt5DBus
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5DBus.so.5
%attr(755,root,root) %{_libdir}/libQt5DBus.so.*.*.*

%files -n Qt5Test
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Test.so.5
%attr(755,root,root) %{_libdir}/libQt5Test.so.*.*.*

%files -n Qt5Concurrent
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Concurrent.so.5
%attr(755,root,root) %{_libdir}/libQt5Concurrent.so.*.*.*

%files -n Qt5Xml
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Xml.so.5
%attr(755,root,root) %{_libdir}/libQt5Xml.so.*.*.*

# qtbase - GUI libraries
%files -n Qt5Gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Gui.so.5

%files -n Qt5OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5OpenGL.so.5
%attr(755,root,root) %{_libdir}/libQt5OpenGL.so.*.*.*

%files -n Qt5PrintSupport
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5PrintSupport.so.5
%attr(755,root,root) %{_libdir}/libQt5PrintSupport.so.*.*.*

%files -n Qt5Widgets
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Widgets.so.5
%attr(755,root,root) %{_libdir}/libQt5Widgets.so.*.*.*

%files -n Qt5Network
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Network.so.5
%attr(755,root,root) %{_libdir}/libQt5Network.so.*.*.*

%files -n Qt5Sql
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Sql.so.5
%attr(755,root,root) %{_libdir}/libQt5Sql.so.*.*.*

%files base -f qtbase.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/accessible
%attr(755,root,root) %{_libdir}/qt5/plugins/accessible/libqtaccessiblewidgets.so

%dir %{_libdir}/qt5/plugins/generic
%attr(755,root,root) %{_libdir}/qt5/plugins/generic/libqevdevkeyboardplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/generic/libqevdevmouseplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/generic/libqevdevtabletplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/generic/libqevdevtouchplugin.so

%dir %{_libdir}/qt5/plugins/iconengines
%dir %{_libdir}/qt5/plugins/imageformats
# qtbase
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqgif.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqico.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqjpeg.so
# qtimageformats
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqdds.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqicns.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqjp2.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqmng.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqtga.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqtiff.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqwbmp.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqwebp.so
# qtsvg
%attr(755,root,root) %{_libdir}/qt5/plugins/iconengines/libqsvgicon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqsvg.so

%dir %{_libdir}/qt5/plugins/platforminputcontexts
%attr(755,root,root) %{_libdir}/qt5/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so

%dir %{_libdir}/qt5/plugins/platforms
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqeglfs.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqkms.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqlinuxfb.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqminimal.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqminimalegl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqoffscreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/libqxcb.so

%dir %{_libdir}/qt5/plugins/platformthemes
%attr(755,root,root) %{_libdir}/qt5/plugins/platformthemes/libqgtk2.so

%dir %{_libdir}/qt5/plugins/printsupport
%attr(755,root,root) %{_libdir}/qt5/plugins/printsupport/libcupsprintersupport.so

%dir %{_libdir}/qt5/plugins/bearer
%attr(755,root,root) %{_libdir}/qt5/plugins/bearer/libqconnmanbearer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/bearer/libqgenericbearer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/bearer/libqnmbearer.so

%dir %{_libdir}/qt5/plugins/sqldrivers
%attr(755,root,root) %{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%files base-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/moc
%attr(755,root,root) %{_bindir}/qdbuscpp2xml
%attr(755,root,root) %{_bindir}/qdbusxml2cpp
%attr(755,root,root) %{_bindir}/qdoc
%attr(755,root,root) %{_bindir}/qlalr
%attr(755,root,root) %{_bindir}/qmake
%attr(755,root,root) %{_bindir}/rcc
%attr(755,root,root) %{_bindir}/syncqt.pl
%attr(755,root,root) %{_bindir}/uic
%attr(755,root,root) %{_libdir}/qt5/bin/moc
%attr(755,root,root) %{_libdir}/qt5/bin/qdbuscpp2xml
%attr(755,root,root) %{_libdir}/qt5/bin/qdbusxml2cpp
%attr(755,root,root) %{_libdir}/qt5/bin/qdoc
%attr(755,root,root) %{_libdir}/qt5/bin/qlalr
%attr(755,root,root) %{_libdir}/qt5/bin/qmake
%attr(755,root,root) %{_libdir}/qt5/bin/rcc
%attr(755,root,root) %{_libdir}/qt5/bin/syncqt.pl
%attr(755,root,root) %{_libdir}/qt5/bin/uic
%attr(755,root,root) %{_libdir}/libQt5Concurrent.so
%attr(755,root,root) %{_libdir}/libQt5Core.so
%attr(755,root,root) %{_libdir}/libQt5DBus.so
%attr(755,root,root) %{_libdir}/libQt5Gui.so
%attr(755,root,root) %{_libdir}/libQt5Network.so
%attr(755,root,root) %{_libdir}/libQt5OpenGL.so
%attr(755,root,root) %{_libdir}/libQt5PrintSupport.so
%attr(755,root,root) %{_libdir}/libQt5Sql.so
%attr(755,root,root) %{_libdir}/libQt5Test.so
%attr(755,root,root) %{_libdir}/libQt5Widgets.so
%attr(755,root,root) %{_libdir}/libQt5Xml.so

%{_libdir}/libQt5Bootstrap.a
%{_libdir}/libQt5OpenGLExtensions.a
%{_libdir}/libQt5PlatformSupport.a
%{_libdir}/libQt5Bootstrap.prl
%{_libdir}/libQt5Concurrent.prl
%{_libdir}/libQt5Core.prl
%{_libdir}/libQt5DBus.prl
%{_libdir}/libQt5Gui.prl
%{_libdir}/libQt5Network.prl
%{_libdir}/libQt5OpenGL.prl
%{_libdir}/libQt5OpenGLExtensions.prl
%{_libdir}/libQt5PlatformSupport.prl
%{_libdir}/libQt5PrintSupport.prl
%{_libdir}/libQt5Sql.prl
%{_libdir}/libQt5Test.prl
%{_libdir}/libQt5Widgets.prl
%{_libdir}/libQt5Xml.prl

%dir %{_includedir}/qt5
%{_includedir}/qt5/QtConcurrent
%{_includedir}/qt5/QtCore
%{_includedir}/qt5/QtDBus
%{_includedir}/qt5/QtGui
%{_includedir}/qt5/QtNetwork
%{_includedir}/qt5/QtOpenGL
%{_includedir}/qt5/QtOpenGLExtensions
%{_includedir}/qt5/QtPlatformSupport
%{_includedir}/qt5/QtPrintSupport
%{_includedir}/qt5/QtSql
%{_includedir}/qt5/QtTest
%{_includedir}/qt5/QtWidgets
%{_includedir}/qt5/QtXml

%{_libdir}/cmake/Qt5
%{_libdir}/cmake/Qt5Concurrent
%{_libdir}/cmake/Qt5Core
%{_libdir}/cmake/Qt5DBus
%{_libdir}/cmake/Qt5Gui
%{_libdir}/cmake/Qt5Network
%{_libdir}/cmake/Qt5OpenGL
%{_libdir}/cmake/Qt5OpenGLExtensions
%{_libdir}/cmake/Qt5PrintSupport
%{_libdir}/cmake/Qt5Sql
%{_libdir}/cmake/Qt5Test
%{_libdir}/cmake/Qt5Widgets
%{_libdir}/cmake/Qt5Xml

%{_pkgconfigdir}/Qt5Bootstrap.pc
%{_pkgconfigdir}/Qt5Concurrent.pc
%{_pkgconfigdir}/Qt5Core.pc
%{_pkgconfigdir}/Qt5DBus.pc
%{_pkgconfigdir}/Qt5Gui.pc
%{_pkgconfigdir}/Qt5Network.pc
%{_pkgconfigdir}/Qt5OpenGLExtensions.pc
%{_pkgconfigdir}/Qt5OpenGL.pc
%{_pkgconfigdir}/Qt5PlatformSupport.pc
%{_pkgconfigdir}/Qt5PrintSupport.pc
%{_pkgconfigdir}/Qt5Sql.pc
%{_pkgconfigdir}/Qt5Test.pc
%{_pkgconfigdir}/Qt5Widgets.pc
%{_pkgconfigdir}/Qt5Xml.pc

%dir %{_libdir}/qt5/mkspecs
%dir %{_libdir}/qt5/mkspecs/modules
%{_libdir}/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_concurrent.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_concurrent_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_core.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_core_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_dbus.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_dbus_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_gui.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_gui_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_network.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_network_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_opengl.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_opengl_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_openglextensions.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_openglextensions_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_platformsupport_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_printsupport.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_printsupport_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_sql.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_sql_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_testlib.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_testlib_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_widgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_widgets_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_xml.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_xml_private.pri
%{_libdir}/qt5/mkspecs/qconfig.pri
%{_libdir}/qt5/mkspecs/qdevice.pri
%{_libdir}/qt5/mkspecs/qfeatures.pri
%{_libdir}/qt5/mkspecs/qmodule.pri

%{_libdir}/qt5/mkspecs/aix-*
%{_libdir}/qt5/mkspecs/android-*
%{_libdir}/qt5/mkspecs/blackberry-*
%{_libdir}/qt5/mkspecs/common
%{_libdir}/qt5/mkspecs/cygwin-*
%{_libdir}/qt5/mkspecs/darwin-*
%{_libdir}/qt5/mkspecs/devices
%{_libdir}/qt5/mkspecs/features
%{_libdir}/qt5/mkspecs/freebsd-*
%{_libdir}/qt5/mkspecs/hpux-*
%{_libdir}/qt5/mkspecs/hpuxi-*
%{_libdir}/qt5/mkspecs/hurd-*
%{_libdir}/qt5/mkspecs/irix-*
%{_libdir}/qt5/mkspecs/linux-*
%{_libdir}/qt5/mkspecs/lynxos-*
%{_libdir}/qt5/mkspecs/macx-*
%{_libdir}/qt5/mkspecs/netbsd-*
%{_libdir}/qt5/mkspecs/openbsd-*
%{_libdir}/qt5/mkspecs/qnx-*
%{_libdir}/qt5/mkspecs/sco-*
%{_libdir}/qt5/mkspecs/solaris-*
%{_libdir}/qt5/mkspecs/tru64-*
%{_libdir}/qt5/mkspecs/unixware-*
%{_libdir}/qt5/mkspecs/unsupported
%{_libdir}/qt5/mkspecs/win32-*
%{_libdir}/qt5/mkspecs/wince60standard-*
%{_libdir}/qt5/mkspecs/wince70embedded-*
%{_libdir}/qt5/mkspecs/winphone-*
%{_libdir}/qt5/mkspecs/winrt-*

# qtconnectivity
%files -n Qt5Bluetooth
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Bluetooth.so.5
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so.*.*.*

%files -n Qt5Nfc
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Nfc.so.5
%attr(755,root,root) %{_libdir}/libQt5Nfc.so.*.*.*

%files declarative-bluetooth
%defattr(644,root,root,755)
%dir  %{_libdir}/qt5/qml/QtBluetooth
%attr(755,root,root) %{_libdir}/qt5/qml/QtBluetooth/libdeclarative_bluetooth.so
%{_libdir}/qt5/qml/QtBluetooth/plugins.qmltypes
%{_libdir}/qt5/qml/QtBluetooth/qmldir

%files declarative-nfc
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/QtNfc
%attr(755,root,root) %{_libdir}/qt5/qml/QtNfc/libdeclarative_nfc.so
%{_libdir}/qt5/qml/QtNfc/plugins.qmltypes
%{_libdir}/qt5/qml/QtNfc/qmldir

%files connectivity-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so
%attr(755,root,root) %{_libdir}/libQt5Nfc.so
%{_includedir}/qt5/QtBluetooth
%{_includedir}/qt5/QtNfc
%{_libdir}/cmake/Qt5Bluetooth
%{_libdir}/cmake/Qt5Nfc
%{_libdir}/libQt5Bluetooth.prl
%{_libdir}/libQt5Nfc.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_bluetooth.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_bluetooth_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_nfc.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_nfc_private.pri
%{_pkgconfigdir}/Qt5Bluetooth.pc
%{_pkgconfigdir}/Qt5Nfc.pc

# qtdeclarative
%files -n Qt5Qml
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Qml.so.5
%attr(755,root,root) %{_libdir}/libQt5Qml.so.*.*.*

%files -n Qt5Quick
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickParticles.so.5
%attr(755,root,root) %ghost %{_libdir}/libQt5Quick.so.5
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickTest.so.5
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickWidgets.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Quick.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5QuickWidgets.so.*.*.*

%files declarative -f qtdeclarative.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/accessible/libqtaccessiblequick.so

%dir %{_libdir}/qt5/plugins/qmltooling
%attr(755,root,root) %{_libdir}/qt5/plugins/qmltooling/libqmldbg_qtquick2.so
%attr(755,root,root) %{_libdir}/qt5/plugins/qmltooling/libqmldbg_tcp.so

%dir %{_libdir}/qt5/qml
%dir %{_libdir}/qt5/qml/Qt
%dir %{_libdir}/qt5/qml/Qt/labs
%dir %{_libdir}/qt5/qml/Qt/labs/folderlistmodel
%attr(755,root,root) %{_libdir}/qt5/qml/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.so
%{_libdir}/qt5/qml/Qt/labs/folderlistmodel/plugins.qmltypes
%{_libdir}/qt5/qml/Qt/labs/folderlistmodel/qmldir

%dir %{_libdir}/qt5/qml/Qt/labs/settings
%attr(755,root,root) %{_libdir}/qt5/qml/Qt/labs/settings/libqmlsettingsplugin.so
%{_libdir}/qt5/qml/Qt/labs/settings/plugins.qmltypes
%{_libdir}/qt5/qml/Qt/labs/settings/qmldir

%dir %{_libdir}/qt5/qml/QtQml
%dir %{_libdir}/qt5/qml/QtQml/Models.2
%attr(755,root,root) %{_libdir}/qt5/qml/QtQml/Models.2/libmodelsplugin.so
%{_libdir}/qt5/qml/QtQml/Models.2/qmldir

%dir %{_libdir}/qt5/qml/QtQuick.2
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick.2/libqtquick2plugin.so
%{_libdir}/qt5/qml/QtQuick.2/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick.2/qmldir

%dir %{_libdir}/qt5/qml/QtQuick
%dir %{_libdir}/qt5/qml/QtQuick/LocalStorage
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/LocalStorage/libqmllocalstorageplugin.so
%{_libdir}/qt5/qml/QtQuick/LocalStorage/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/LocalStorage/qmldir

%dir %{_libdir}/qt5/qml/QtQuick/Particles.2
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/Particles.2/libparticlesplugin.so
%{_libdir}/qt5/qml/QtQuick/Particles.2/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/Particles.2/qmldir

%dir %{_libdir}/qt5/qml/QtQuick/Window.2
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/Window.2/libwindowplugin.so
%{_libdir}/qt5/qml/QtQuick/Window.2/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/Window.2/qmldir

%dir %{_libdir}/qt5/qml/QtQuick/XmlListModel
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/XmlListModel/libqmlxmllistmodelplugin.so
%{_libdir}/qt5/qml/QtQuick/XmlListModel/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/XmlListModel/qmldir

%dir %{_libdir}/qt5/qml/QtTest
%attr(755,root,root) %{_libdir}/qt5/qml/QtTest/libqmltestplugin.so
%{_libdir}/qt5/qml/QtTest/SignalSpy.qml
%{_libdir}/qt5/qml/QtTest/TestCase.qml
%{_libdir}/qt5/qml/QtTest/plugins.qmltypes
%{_libdir}/qt5/qml/QtTest/qmldir
%{_libdir}/qt5/qml/QtTest/testlogger.js

# qtgraphicaleffects
%files graphicaleffects
%defattr(644,root,root,755)
%{_libdir}/qt5/qml/QtGraphicalEffects

# qtquickcontrols
%files quickcontrols
%defattr(644,root,root,755)
%{_libdir}/qt5/qml/QtQuick/Controls
%dir %{_libdir}/qt5/qml/QtQuick/Dialogs
%dir %{_libdir}/qt5/qml/QtQuick/Dialogs/Private
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.so
%{_libdir}/qt5/qml/QtQuick/Dialogs/Private/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.so
%{_libdir}/qt5/qml/QtQuick/Dialogs/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/Dialogs/qmldir

%dir %{_libdir}/qt5/qml/QtQuick/Layouts
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/Layouts/libqquicklayoutsplugin.so
%{_libdir}/qt5/qml/QtQuick/Layouts/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/Layouts/qmldir

%dir %{_libdir}/qt5/qml/QtQuick/PrivateWidgets
%attr(755,root,root) %{_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.so
%{_libdir}/qt5/qml/QtQuick/PrivateWidgets/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/PrivateWidgets/qmldir

%files declarative-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qml
%attr(755,root,root) %{_bindir}/qmlbundle
%attr(755,root,root) %{_bindir}/qmlimportscanner
%attr(755,root,root) %{_bindir}/qmlmin
%attr(755,root,root) %{_bindir}/qmlplugindump
%attr(755,root,root) %{_bindir}/qmlprofiler
%attr(755,root,root) %{_bindir}/qmlscene
%attr(755,root,root) %{_bindir}/qmltestrunner
%attr(755,root,root) %{_libdir}/qt5/bin/qml
%attr(755,root,root) %{_libdir}/qt5/bin/qmlbundle
%attr(755,root,root) %{_libdir}/qt5/bin/qmlimportscanner
%attr(755,root,root) %{_libdir}/qt5/bin/qmlmin
%attr(755,root,root) %{_libdir}/qt5/bin/qmlplugindump
%attr(755,root,root) %{_libdir}/qt5/bin/qmlprofiler
%attr(755,root,root) %{_libdir}/qt5/bin/qmlscene
%attr(755,root,root) %{_libdir}/qt5/bin/qmltestrunner
%attr(755,root,root) %{_libdir}/libQt5Qml.so
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so
%attr(755,root,root) %{_libdir}/libQt5Quick.so
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so
%attr(755,root,root) %{_libdir}/libQt5QuickWidgets.so
%{_libdir}/libQt5QmlDevTools.a
%{_includedir}/qt5/QtQml
%{_includedir}/qt5/QtQuick
%{_includedir}/qt5/QtQuickParticles
%{_includedir}/qt5/QtQuickTest
%{_includedir}/qt5/QtQuickWidgets
%{_libdir}/cmake/Qt5Qml
%{_libdir}/cmake/Qt5Quick
%{_libdir}/cmake/Qt5QuickTest
%{_libdir}/cmake/Qt5QuickWidgets
%{_libdir}/libQt5Qml.prl
%{_libdir}/libQt5QmlDevTools.prl
%{_libdir}/libQt5Quick.prl
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/libQt5QuickWidgets.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_qml.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_qml_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmltest.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmltest_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_quick.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_quick_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_quickwidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri
%{_pkgconfigdir}/Qt5Qml.pc
%{_pkgconfigdir}/Qt5QmlDevTools.pc
%{_pkgconfigdir}/Qt5Quick.pc
%{_pkgconfigdir}/Qt5QuickParticles.pc
%{_pkgconfigdir}/Qt5QuickTest.pc
%{_pkgconfigdir}/Qt5QuickWidgets.pc

# qtpositioning
%files -n Qt5Positioning
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Positioning.so.5
%attr(755,root,root) %{_libdir}/libQt5Positioning.so.*.*.*

%files location -f qtlocation.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/position
%attr(755,root,root) %{_libdir}/qt5/plugins/position/libqtposition_positionpoll.so

%files declarative-location
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/QtPositioning
%attr(755,root,root) %{_libdir}/qt5/qml/QtPositioning/libdeclarative_positioning.so
%{_libdir}/qt5/qml/QtPositioning/plugins.qmltypes
%{_libdir}/qt5/qml/QtPositioning/qmldir

%files location-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Positioning.so
%{_includedir}/qt5/QtPositioning
%{_libdir}/cmake/Qt5Positioning
%{_libdir}/libQt5Positioning.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_positioning.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_positioning_private.pri
%{_pkgconfigdir}/Qt5Positioning.pc

# qtsensors
%files -n Qt5Sensors
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Sensors.so.5
%attr(755,root,root) %{_libdir}/libQt5Sensors.so.*.*.*

%files sensors
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/sensors
%attr(755,root,root) %{_libdir}/qt5/plugins/sensors/libqtsensors_dummy.so
%attr(755,root,root) %{_libdir}/qt5/plugins/sensors/libqtsensors_generic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/sensors/libqtsensors_linuxsys.so
%dir %{_libdir}/qt5/plugins/sensorgestures
%attr(755,root,root) %{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_plugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_shakeplugin.so

%files declarative-sensors
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/QtSensors
%attr(755,root,root) %{_libdir}/qt5/qml/QtSensors/libdeclarative_sensors.so
%{_libdir}/qt5/qml/QtSensors/plugins.qmltypes
%{_libdir}/qt5/qml/QtSensors/qmldir

%files sensors-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Sensors.so
%{_includedir}/qt5/QtSensors
%{_libdir}/cmake/Qt5Sensors
%{_libdir}/libQt5Sensors.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_sensors.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_sensors_private.pri
%{_pkgconfigdir}/Qt5Sensors.pc

# qtsvg
%files -n Qt5Svg
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Svg.so.5
%attr(755,root,root) %{_libdir}/libQt5Svg.so.*.*.*

%files svg-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Svg.so
%{_includedir}/qt5/QtSvg
%{_libdir}/cmake/Qt5Svg
%{_libdir}/libQt5Svg.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_svg.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_svg_private.pri
%{_pkgconfigdir}/Qt5Svg.pc

# qttools
%files -n Qt5Designer
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Designer.so.5
%attr(755,root,root) %ghost %{_libdir}/libQt5DesignerComponents.so.5
%attr(755,root,root) %{_libdir}/libQt5Designer.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so.*.*.*

%files -n Qt5Help
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Help.so.5
%attr(755,root,root) %{_libdir}/libQt5Help.so.*.*.*

%files -n Qt5CLucene
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5CLucene.so.5
%attr(755,root,root) %{_libdir}/libQt5CLucene.so.*.*.*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtdiag
%attr(755,root,root) %{_bindir}/qtpaths
%attr(755,root,root) %{_libdir}/qt5/bin/qtdiag
%attr(755,root,root) %{_libdir}/qt5/bin/qtpaths

%files tools-assistant -f assistant.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assistant
%attr(755,root,root) %{_bindir}/pixeltool
%attr(755,root,root) %{_bindir}/qcollectiongenerator
%attr(755,root,root) %{_libdir}/qt5/bin/assistant
%attr(755,root,root) %{_libdir}/qt5/bin/pixeltool
%attr(755,root,root) %{_libdir}/qt5/bin/qcollectiongenerator

%files tools-qdbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qdbus
%attr(755,root,root) %{_bindir}/qdbusviewer
%attr(755,root,root) %{_libdir}/qt5/bin/qdbus
%attr(755,root,root) %{_libdir}/qt5/bin/qdbusviewer

%files tools-designer -f designer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/designer
%attr(755,root,root) %{_libdir}/qt5/bin/designer
%dir %attr(755,root,root) %{_libdir}/qt5/plugins/designer
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqquickwidget.so
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqwebview.so

%files tools-help
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qhelpconverter
%attr(755,root,root) %{_bindir}/qhelpgenerator
%attr(755,root,root) %{_libdir}/qt5/bin/qhelpconverter
%attr(755,root,root) %{_libdir}/qt5/bin/qhelpgenerator

%files tools-linguist -f linguist.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lconvert
%attr(755,root,root) %{_bindir}/linguist
%attr(755,root,root) %{_bindir}/lrelease
%attr(755,root,root) %{_bindir}/lupdate
%attr(755,root,root) %{_libdir}/qt5/bin/lconvert
%attr(755,root,root) %{_libdir}/qt5/bin/linguist
%attr(755,root,root) %{_libdir}/qt5/bin/lrelease
%attr(755,root,root) %{_libdir}/qt5/bin/lupdate
%{_datadir}/qt5/phrasebooks

%files tools-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so
%attr(755,root,root) %{_libdir}/libQt5Designer.so
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so
%attr(755,root,root) %{_libdir}/libQt5Help.so
%{_libdir}/libQt5UiTools.a
%{_includedir}/qt5/QtCLucene
%{_includedir}/qt5/QtDesigner
%{_includedir}/qt5/QtDesignerComponents
%{_includedir}/qt5/QtHelp
%{_includedir}/qt5/QtUiTools
%{_libdir}/cmake/Qt5Designer
%{_libdir}/cmake/Qt5Help
%{_libdir}/cmake/Qt5LinguistTools
%{_libdir}/cmake/Qt5UiTools
%{_libdir}/libQt5CLucene.prl
%{_libdir}/libQt5Designer.prl
%{_libdir}/libQt5DesignerComponents.prl
%{_libdir}/libQt5Help.prl
%{_libdir}/libQt5UiTools.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_clucene_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_designer.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_designer_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_help.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{_pkgconfigdir}/Qt5CLucene.pc
%{_pkgconfigdir}/Qt5Designer.pc
%{_pkgconfigdir}/Qt5DesignerComponents.pc
%{_pkgconfigdir}/Qt5Help.pc
%{_pkgconfigdir}/Qt5UiTools.pc

# qtwebkit
%files -n Qt5WebKit
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5WebKit.so.5
%attr(755,root,root) %ghost %{_libdir}/libQt5WebKitWidgets.so.5
%attr(755,root,root) %{_libdir}/libQt5WebKit.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so.*.*.*

%files webkit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/QtWebPluginProcess
%attr(755,root,root) %{_libdir}/qt5/QtWebProcess

%files declarative-webkit
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/QtWebKit
%dir %{_libdir}/qt5/qml/QtWebKit/experimental
%{_libdir}/qt5/qml/QtWebKit/experimental/libqmlwebkitexperimentalplugin.so
%{_libdir}/qt5/qml/QtWebKit/experimental/qmldir
%{_libdir}/qt5/qml/QtWebKit/libqmlwebkitplugin.so
%{_libdir}/qt5/qml/QtWebKit/plugins.qmltypes
%{_libdir}/qt5/qml/QtWebKit/qmldir

%files webkit-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebKit.so
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so
%{_includedir}/qt5/QtWebKit
%{_includedir}/qt5/QtWebKitWidgets
%{_libdir}/cmake/Qt5WebKit
%{_libdir}/cmake/Qt5WebKitWidgets
%{_libdir}/libQt5WebKit.prl
%{_libdir}/libQt5WebKitWidgets.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_webkit.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webkit_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webkitwidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webkitwidgets_private.pri
%{_pkgconfigdir}/Qt5WebKit.pc
%{_pkgconfigdir}/Qt5WebKitWidgets.pc

# qtxmlpatterns
%files -n Qt5XmlPatterns -f qtxmlpatterns.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5XmlPatterns.so.5
%attr(755,root,root) %{_libdir}/libQt5XmlPatterns.so.*.*.*

%files xmlpatterns-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlpatterns
%attr(755,root,root) %{_bindir}/xmlpatternsvalidator
%attr(755,root,root) %{_libdir}/qt5/bin/xmlpatterns
%attr(755,root,root) %{_libdir}/qt5/bin/xmlpatternsvalidator
%attr(755,root,root) %{_libdir}/libQt5XmlPatterns.so
%{_includedir}/qt5/QtXmlPatterns
%{_libdir}/cmake/Qt5XmlPatterns
%{_libdir}/libQt5XmlPatterns.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_xmlpatterns.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_xmlpatterns_private.pri
%{_pkgconfigdir}/Qt5XmlPatterns.pc

%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/qt5
%{_docdir}/qt5/global

