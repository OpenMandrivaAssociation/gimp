#define _disable_ld_as_needed   1
# optional compile flags
%define enable_python 1
%{?_without_python: %global enable_python 0}

%define enable_lzw 0
%{?_with_lzw: %global enable_lzw 1}

%define	api	2.0
%define	abi	2.8
%define	major	0
%define	libname 	%mklibname %{name} %{api}_%{major}
%define	libbase		%mklibname gimpbase %{api} %{major}
%define	libcolor	%mklibname gimpcolor %{api} %{major}
%define	libconfig	%mklibname gimpconfig %{api} %{major}
%define	libmath		%mklibname gimpmath %{api} %{major}
%define	libmodule	%mklibname gimpmodule %{api} %{major}
%define	libthumb	%mklibname gimpthumb %{api} %{major}
%define	libui		%mklibname gimpui %{api} %{major}
%define	libwidgets	%mklibname gimpwidgets %{api} %{major}
%define	devname 	%mklibname -d %{name}%{api}

Summary:	The GNU Image Manipulation Program
Name:		gimp
Epoch:		1
Version:	2.8.6
Release:	3
License:	GPLv2+
Group:		Graphics
Url:		http://www.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2
Source1:	ftp://ftp.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2.md5
Source13:	gimp-scripting-sample.pl
Patch0:		gimp-2.5.1-desktopentry.patch
Patch1:		gimp-2.8.4-link.patch

BuildRequires:	desktop-file-utils
BuildRequires:	iso-codes
BuildRequires:	gtk-doc
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	perl
BuildRequires:	aalib-devel
BuildRequires:	jasper-devel
BuildRequires:	libwmf-devel >= 0.2.8
BuildRequires:	mng-devel
BuildRequires:	tiff-devel
BuildRequires:	bzip2-devel
BuildRequires:	ghostscript-devel
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gegl-0.2)
BuildRequires:	pkgconfig(atk) >= 2.2.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.30.2
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(libcurl)
# help browser
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
# mail plugin
BuildRequires:	postfix #sendmail-command
# print plugin
#BuildRequires: libgimpprint-devel >= 4.2.0
# python plugin
%if %{enable_python}
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python)
%endif
# Require gegl, otherwise GIMP crashes on some operations
# (at least on cage transformation)
Requires:	gegl
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

%package -n %{libname}
Summary:	GIMP libraries
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{libbase}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libbase}
This package contains a shared library for %{name}.

%package -n %{libcolor}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libcolor}
This package contains a shared library for %{name}.

%package -n %{libconfig}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libconfig}
This package contains a shared library for %{name}.

%package -n %{libmath}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libmath}
This package contains a shared library for %{name}.

%package -n %{libmodule}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libmodule}
This package contains a shared library for %{name}.

%package -n %{libthumb}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libthumb}
This package contains a shared library for %{name}.

%package -n %{libui}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libui}
This package contains a shared library for %{name}.

%package -n %{libwidgets}
Summary:	GIMP libraries
Group:		System/Libraries
Conflicts:	%{_lib}gimp2.0_0 < 1:2.8.4-2

%description -n %{libwidgets}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	GIMP plugin and extension development kit
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Requires:	%{libbase} = %{EVRD}
Requires:	%{libcolor} = %{EVRD}
Requires:	%{libconfig} = %{EVRD}
Requires:	%{libmath} = %{EVRD}
Requires:	%{libmodule} = %{EVRD}
Requires:	%{libthumb} = %{EVRD}
Requires:	%{libui} = %{EVRD}
Requires:	%{libwidgets} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}

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
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-default-binary=yes \
	--enable-mp=yes \
%if %{enable_python}
	--enable-python=yes \
%else
	--enable-python=no \
%endif
%if %{enable_lzw}
	--with-gif-compression=lzw \
%else
	--with-gif-compression=rle \
%endif
	--without-hal \
	--with-gvfs \
	--with-dbus \
	--enable-gtk-doc=yes

%make

%install
%makeinstall_std

#clean unpackaged files
#rm -f %{buildroot}%{_libdir}/gimp/%{api}/*/*.a
#find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

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

%files -n %{libname}
%{_libdir}/libgimp-%{api}.so.%{major}*

%files -n %{libbase}
%{_libdir}/libgimpbase-%{api}.so.%{major}*

%files -n %{libcolor}
%{_libdir}/libgimpcolor-%{api}.so.%{major}*

%files -n %{libconfig}
%{_libdir}/libgimpconfig-%{api}.so.%{major}*

%files -n %{libmath}
%{_libdir}/libgimpmath-%{api}.so.%{major}*

%files -n %{libmodule}
%{_libdir}/libgimpmodule-%{api}.so.%{major}*

%files -n %{libthumb}
%{_libdir}/libgimpthumb-%{api}.so.%{major}*

%files -n %{libui}
%{_libdir}/libgimpui-%{api}.so.%{major}*

%files -n %{libwidgets}
%{_libdir}/libgimpwidgets-%{api}.so.%{major}*

%if %{enable_python}
%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/gimptool-*
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/gimptool-*

%files python
%{_libdir}/gimp/%{api}/environ/pygimp.env
%{_libdir}/gimp/%{api}/python
%{_libdir}/gimp/%{api}/plug-ins/*.py
%{_libdir}/python%{py_ver}/site-packages/*.pth
%endif

