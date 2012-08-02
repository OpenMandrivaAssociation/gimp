%define _disable_ld_as_needed   1
# optional compile flags
%define enable_python 1
%{?_without_python: %global enable_python 0}

%define enable_lzw 0
%{?_with_lzw: %global enable_lzw 1}

%define api 2.0
%define abi 2.8
%define major 0
%define libname	%mklibname %{name} %{api}_%{major}
%define develname %mklibname -d %{name}%{api}

Summary:	The GNU Image Manipulation Program
Name:		gimp
Epoch:		1
Version:	2.8.0
Release:	2
License:	GPLv2+
Group:		Graphics
URL:		http://www.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2
Source1:	ftp://ftp.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2.md5
Source13:	gimp-scripting-sample.pl
Patch0:		gimp-2.5.1-desktopentry.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gtk-doc
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	perl
BuildRequires:	aalib-devel
BuildRequires:	jasper-devel
BuildRequires:	libwmf-devel >= 0.2.8
BuildRequires:	mng-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(alsa)
Buildrequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gegl-0.2)
BuildRequires:	pkgconfig(atk) >= 2.2.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.30.2
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(poppler-glib)
# help browser
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
# mail plugin
BuildRequires:	sendmail-command
# print plugin
#BuildRequires: libgimpprint-devel >= 4.2.0
# python plugin
%if %{enable_python}
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	python-devel
%endif
# Require gegl, otherwise GIMP crashes on some operations
# (at least on cage transformation)
Requires:	gegl

Requires(post,postun): desktop-file-utils
Suggests:	gimp-help-2

%rename gimp2.6

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
--without python        Disable pygimp (default enabled)
--with    lzw           Enable LZW compression in GIF (default disabled)

%package -n %{develname}
Summary:	GIMP plugin and extension development kit
Group:		Development/GNOME and GTK+
License:	LGPLv2+
Requires:	%{libname} >= %{EVRD}
Provides:	gimp-devel = %{version}-%{release}

%description -n %{develname}
Static libraries and header files for writing GIMP plugins and extensions.

%package -n %{libname}
Summary:	GIMP libraries
Group:		System/Libraries
License:	LGPLv2+

%description -n %{libname}
This is the library that provides core GIMP functionality.
It enable other programs to use GIMP's features but is mainly intended
to be used by the GIMP and its "external" plugins.

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

%setup -q
%apply_patches

%build
%configure \
	--disable-static \
	--enable-default-binary=yes \
	--enable-mp=yes		\
%if %{enable_python}
	--enable-python=yes	\
%else
	--enable-python=no	\
%endif
%if %enable_lzw
	--with-gif-compression=lzw	\
%else
	--with-gif-compression=rle	\
%endif
	--without-hal \
	--with-gvfs \
	--with-dbus \
	--enable-gtk-doc=yes

%make

%install
%makeinstall_std

#clean unpackaged files
rm -f %{buildroot}%{_libdir}/gimp/%{api}/*/*.a
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# workaround broken help system
HELP_DIR=%{buildroot}%{_datadir}/gimp/%api/help/C
[[ -d $HELP_DIR ]] || mkdir -p $HELP_DIR
HELP_IDX=$HELP_DIR/introduction.html
echo -e '<HTML><HEAD><TITLE>GIMP Base Library</HEAD>\n<BODY><UL>' > $HELP_IDX

/bin/ls %{buildroot}%{_datadir}/gtk-doc/html/*/index.html | sed -e "s@%{buildroot}@@g" >> $HELP_IDX
perl -pi -e 's!(.*/html/)([^/]*)(/index.html)!<LI><A HREF="\1\2\3">\2</A>!g' $HELP_IDX

echo '</UL></BODY></HTML>' >> $HELP_IDX

%find_lang gimp20 --all-name

%if %{enable_python}
chmod 755 %{buildroot}%{_libdir}/gimp/%{api}/plug-ins/*.py
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
%dir %{_libdir}/gimp/%{api}
%dir %{_libdir}/gimp/%{api}/environ
%{_libdir}/gimp/%{api}/interpreters
%{_libdir}/gimp/%{api}/environ/default.env
%{_libdir}/gimp/%{api}/modules
%{_libdir}/gimp/%{api}/plug-ins
%exclude %{_libdir}/gimp/%{api}/plug-ins/*.py
%{_datadir}/applications/*
%{_datadir}/gimp
%{_datadir}/icons/hicolor/*/apps/gimp.png
%{_mandir}/man1/gimp-*
%{_mandir}/man1/gimp.*
%{_mandir}/man5/gimp*

%files -n %{develname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/gimptool-*
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/gimptool-*

%files -n %{libname}
# explicitly list all libs to avoid old libtool issue
# MD these should be split up
%{_libdir}/libgimpconfig-%{api}.so.%{major}*
%{_libdir}/libgimp-%{api}.so.%{major}*
%{_libdir}/libgimpthumb-%{api}.so.%{major}*
%{_libdir}/libgimpbase-%{api}.so.%{major}*
%{_libdir}/libgimpcolor-%{api}.so.%{major}*
%{_libdir}/libgimpmath-%{api}.so.%{major}*
%{_libdir}/libgimpmodule-%{api}.so.%{major}*
%{_libdir}/libgimpui-%{api}.so.%{major}*
%{_libdir}/libgimpwidgets-%{api}.so.%{major}*

%if %{enable_python}
%files python
%{_libdir}/gimp/%{api}/environ/pygimp.env
%{_libdir}/gimp/%{api}/python
%{_libdir}/gimp/%{api}/plug-ins/*.py
%{_libdir}/python%{py_ver}/site-packages/*.pth
%endif
