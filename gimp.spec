%bcond_with	python
%global optflags %{optflags} -O3 -Wno-int-conversion

%define api 2.0
%define abi 2.10
%define major 0
%define oldlibname %mklibname %{name} %{api}_%{major}
%define oldlibbase %mklibname gimpbase %{api} %{major}
%define oldlibcolor %mklibname gimpcolor %{api} %{major}
%define oldlibconfig %mklibname gimpconfig %{api} %{major}
%define oldlibmath %mklibname gimpmath %{api} %{major}
%define oldlibmodule %mklibname gimpmodule %{api} %{major}
%define oldlibthumb %mklibname gimpthumb %{api} %{major}
%define oldlibui %mklibname gimpui %{api} %{major}
%define oldlibwidgets %mklibname gimpwidgets %{api} %{major}
%define devname %mklibname -d %{name}%{api}

Summary:	The GNU Image Manipulation Program
Name:		gimp
Version:	2.10.36
Release:	6
License:	GPLv2+
Group:		Graphics
Url:		https://www.gimp.org/
Source0:	https://download.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2
#Source1:	http://download.gimp.org/pub/gimp/v%%{abi}/gimp-%%{version}.tar.bz2.md5
Source13:	gimp-scripting-sample.pl
Patch0:		gimp-2.5.1-desktopentry.patch

# Upstream patches
Patch1:		0001-Build-with-mypaint-brushes-2.0.patch
Patch2:		https://gitlab.gnome.org/GNOME/gimp/-/commit/d7228727d7a4b11909001cf8fd8977d68bd29720.patch

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(atk) >= 2.2.0
BuildRequires:	pkgconfig(babl-0.1) >= 0.1.100
BuildRequires:	pkgconfig(cairo) >= 1.10.2
BuildRequires:	pkgconfig(cairo-pdf) >= 1.10.2
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:	pkgconfig(fontconfig) >= 2.2.0
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.24.1
BuildRequires:	pkgconfig(gegl-0.4)
BuildRequires:	pkgconfig(gexiv2) >= 0.10.6
BuildRequires:	pkgconfig(gio-2.0) >= 2.30.2
BuildRequires:	pkgconfig(glib-2.0) >= 2.30.2
BuildRequires:	pkgconfig(gmodule-no-export-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.24.10
BuildRequires:	pkgconfig(gudev-1.0) >= 167
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libavif)
BuildRequires:	pkgconfig(lcms2) >= 2.2
BuildRequires:	pkgconfig(libcurl) >= 7.15.1
BuildRequires:	pkgconfig(libexif) >= 0.6.15
BuildRequires:	pkgconfig(libmypaint) >= 1.5.1
BuildRequires:	pkgconfig(mypaint-brushes-2.0)
BuildRequires:	pkgconfig(libpng) >= 1.2.37
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.36.0
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(pangocairo) >= 1.29.4
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(poppler-glib) >= 0.14.0
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	iso-codes
BuildRequires:	gegl
BuildRequires:	glib-networking
BuildRequires:	gtk-doc
BuildRequires:	gtk+2.0
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	perl
BuildRequires:	aalib-devel
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libwmf)
BuildRequires:	pkgconfig(libmng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	ghostscript-devel
BuildRequires:	pkgconfig(poppler-data)
BuildRequires:	gtk-update-icon-cache
BuildRequires:	x11-server-xvfb
BuildRequires:	glibc-static-devel
# mail plugin
BuildRequires:	sendmail-command
# print plugin
#BuildRequires: libgimpprint-devel >= 4.2.0
# python plugin
%if %{with python}
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python2)
#BuildRequires:	pkgconfig(pycairo)
%endif
# Require gegl, otherwise GIMP crashes on some operations
# (at least on cage transformation)
Requires:	gegl
Requires:	xdg-utils
# Graphviz is now required or GIMP refuse to start due error:
# GIMP requires the GEGL operation "gegl:itrospect".
Requires:	graphviz
Suggests:	gimp-help-2

Requires:	lib64gtk-modules2.0
Requires:	lib64gail18

# No point in splitting out internal helper libraries...
# Not using %%rename because that only obsoletes "older"
# versions and we've dropped an Epoch.
Obsoletes: %{oldlibname}
Obsoletes: %{oldlibbase}
Obsoletes: %{oldlibcolor}
Obsoletes: %{oldlibconfig}
Obsoletes: %{oldlibmath}
Obsoletes: %{oldlibmodule}
Obsoletes: %{oldlibthumb}
Obsoletes: %{oldlibui}
Obsoletes: %{oldlibwidgets}


%description
The GIMP is an image manipulation program suitable for photo retouching,
image composition and image authoring.  Many people find it extremely useful
in creating logos and other graphics for web pages.  The GIMP has many of the
tools and filters you would expect to find in similar commercial offerings,
and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including channel
operations and layers, effects, sub-pixel imaging and anti-aliasing,
and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of the
included scripts rely on fonts that we cannot distribute.  The GIMP ftp
site has a package of fonts that you can install by yourself, which
includes all the fonts needed to run the included scripts.  Some of the
fonts have unusual licensing requirements; all the licenses are documented
in the package.  Get them in ftp://ftp.gimp.org/pub/gimp/fonts/ if you are so
inclined.  Alternatively, choose fonts which exist on your system before
running the scripts.


Build Options:
--with python        Disable pygimp (default disabled, because it requires obsolete python 2.x)

%package -n %{devname}
Summary:	GIMP plugin and extension development kit
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{EVRD}
Requires:	pkgconfig(gegl-0.4)
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development libraries and header files for writing GIMP plugins and extensions.

%package python
Summary:	GIMP python extension
Group:		Graphics
Requires:	pygtk2.0

%description python
This package contains the python modules for GIMP, which act as a
wrapper to libgimp allowing the writing of plug-ins for Gimp.
This is similar to script-fu, except that you can use the full set
of Python extension modules from the plug-in, and you write plug-in
in python instead of in scheme.

%prep
%autosetup -p1
autoupdate
autoreconf -fiv

%build
%configure \
	--enable-default-binary=yes \
	--enable-gimp-console \
	--enable-mp=yes \
%if %{with python}
	--enable-python=yes \
%else
	--enable-python=no \
%endif
	--enable-gtk-doc=yes \
	--with-pdbgen \
	--with-print \
	--with-aa \
	--with-linux-input \
	--without-webkit \
	--with-libmng \
	--with-libxpm \
	--with-alsa \
	--with-cairo-pdf \
	--with-bug-report-url=https://issues.openmandriva.org

%make_build

%install
%make_install

# workaround broken help system
HELP_DIR=%{buildroot}%{_datadir}/gimp/%api/help/C
[[ -d $HELP_DIR ]] || mkdir -p $HELP_DIR
HELP_IDX=$HELP_DIR/introduction.html
echo -e '<HTML><HEAD><TITLE>GIMP Base Library</HEAD>\n<BODY><UL>' > $HELP_IDX

/bin/ls %{buildroot}%{_datadir}/gtk-doc/html/*/index.html | sed -e "s@%{buildroot}@@g" >> $HELP_IDX
perl -pi -e 's!(.*/html/)([^/]*)(/index.html)!<LI><A HREF="\1\2\3">\2</A>!g' $HELP_IDX

echo '</UL></BODY></HTML>' >> $HELP_IDX

%find_lang gimp20 --all-name

%if %{with python}
chmod 755 %{buildroot}%{_libdir}/gimp/%{api}/plug-ins/*/*.py
mkdir -p %{buildroot}%{_libdir}/python%{py_ver}/site-packages
echo %{_libdir}/gimp/%{api}/python > %{buildroot}%{_libdir}/python%{py_ver}/site-packages/gimp.pth
echo %{_libdir}/gimp/%{api}/plug-ins >> %{buildroot}%{_libdir}/python%{py_ver}/site-packages/gimp.pth
%endif

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-CrossDesktop" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%files -f gimp20.lang
%doc AUTHORS NEWS README README.i18n docs/Wilber*
%config(noreplace) %{_sysconfdir}/gimp
%{_bindir}/gimp
%{_bindir}/gimp-%{abi}
%{_bindir}/gimp-console
%{_bindir}/gimp-console-%{abi}
%{_bindir}/gimp-test-clipboard-%{api}
%{_libexecdir}/gimp-debug-tool-2.0
%dir %{_libdir}/gimp/%{api}
%dir %{_libdir}/gimp/%{api}/environ
%{_libdir}/gimp/%{api}/interpreters
%{_libdir}/gimp/%{api}/environ/default.env
%{_libdir}/gimp/%{api}/modules
%{_libdir}/gimp/%{api}/plug-ins
%if %{with python}
%exclude %{_libdir}/gimp/%{api}/plug-ins/*/*.py
%endif
%{_datadir}/applications/*
%{_datadir}/metainfo/*.xml
%{_datadir}/gimp
%{_datadir}/icons/hicolor/*/apps/gimp.png
%{_mandir}/man1/gimp-*
%{_mandir}/man1/gimp.*
%{_mandir}/man5/gimp*
%{_libdir}/libgimp-%{api}.so.%{major}*
%{_libdir}/libgimpbase-%{api}.so.%{major}*
%{_libdir}/libgimpcolor-%{api}.so.%{major}*
%{_libdir}/libgimpconfig-%{api}.so.%{major}*
%{_libdir}/libgimpmath-%{api}.so.%{major}*
%{_libdir}/libgimpmodule-%{api}.so.%{major}*
%{_libdir}/libgimpthumb-%{api}.so.%{major}*
%{_libdir}/libgimpui-%{api}.so.%{major}*
%{_libdir}/libgimpwidgets-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/gimptool-*
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/gimptool-*

%if %{with python}
%files python
%{_libdir}/gimp/%{api}/environ/pygimp.env
%{_libdir}/gimp/%{api}/python
%{_libdir}/gimp/%{api}/plug-ins/*/*.py
%{_libdir}/python%{py_ver}/site-packages/*.pth
%endif
