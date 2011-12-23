# optional compile flags
%define enable_python 1
%{?_without_python: %global enable_python 0}

%define enable_lzw 0
%{?_with_lzw: %global enable_lzw 1}

%define api 2.0
%define abi 2.6
%define major 0
%define libname	%mklibname %{name} %{api}_%{major}
%define develname %mklibname -d %{name}%{api}

Summary:	The GNU Image Manipulation Program
Name:		gimp
Epoch:		1
Version:	2.6.11
Release:	11
License:	GPLv2+
Group:		Graphics
URL:		http://www.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2
Source1:	ftp://ftp.gimp.org/pub/gimp/v%{abi}/gimp-%{version}.tar.bz2.md5
Source13:	gimp-scripting-sample.pl
Patch0:		gimp-2.6.4-fix-str-fmt.patch
Patch1:		gimp-2.6.4-fix-linking.patch
#gw fix name in desktop file and disable startup notification
Patch6:		gimp-2.5.1-desktopentry.patch
# distro specific: use xdg-open instead of firefox as web browser
Patch10:	gimp-2.6.2-xdg-open.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=559081
# "JPEG Save dialog preview should adjust size units"
Patch11:	gimp-2.6.7-jpeg-units.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=556896
# "Dialogs don't get minimized with single image window"
Patch12:	gimp-2.6.6-minimize-dialogs.patch
# backport: fix building with "gold" linker
Patch13:	gimp-2.6.8-gold.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=198367
# https://bugzilla.gnome.org/show_bug.cgi?id=623045
# make script-fu logging IPv6 aware
Patch14:	gimp-2.6.10-script-fu-ipv6.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=651002
# avoid traceback in colorxhtml plugin, upstreamed
Patch15:	gimp-2.6.11-colorxhtml.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=667958
# avoid traceback in pyslice plugin, upstreamed
Patch16:	gimp-2.6.11-pyslice.patch
# backport: work with poppler-0.17, upstreamed
Patch17:	gimp-2.6.11-poppler-0.17.patch
# backport: CVE-2010-4543, CVE-2011-1782
# harden PSP plugin against bogus input data
Patch18:	gimp-2.6.11-psp-overflow.patch
# backport: CVE-2010-4540, CVE-2010-4541, CVE-2010-4542
# fix buffer overflows in sphere-designer, gfig, lighting plugins
Patch19:	gimp-2.6.11-CVE-2010-4540,4541,4542.patch
Patch20:	gimp-2.6.11-CVE-2011-2896.diff
# files changed by autoreconf after applying the above
Patch100:	gimp-2.6.11-11-autoreconf.patch.bz2
Patch101:	gimp-2.6.11-libpng15.diff

BuildRequires: desktop-file-utils
BuildRequires: gtk-doc >= 1.11-3mdv
BuildRequires: imagemagick
BuildRequires: intltool
BuildRequires: perl
BuildRequires: aalib-devel
BuildRequires: libwmf-devel >= 0.2.8
BuildRequires: mng-devel
BuildRequires: tiff-devel
BuildRequires: pkgconfig(alsa)
Buildrequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gegl)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libart-2.0)
BuildRequires: pkgconfig(lcms)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(libpng15)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(poppler-glib)
# help browser
BuildRequires: pkgconfig(webkit-1.0)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xpm)
# mail plugin
BuildRequires: sendmail-command
# print plugin
#BuildRequires: libgimpprint-devel >= 4.2.0
# python plugin
%if %{enable_python}
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: python-devel
%endif

Requires(post,postun): desktop-file-utils
Suggests: gimp-help-2

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

#needed by patch1
autoreconf -fi -I m4macros

%build
%configure2_5x \
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
rm -fr %{buildroot}

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
mkdir -p %{buildroot}%{_libdir}/python%{pyver}/site-packages
echo %{_libdir}/gimp/%{api}/python > %{buildroot}%{_libdir}/python%{pyver}/site-packages/gimp.pth
echo %{_libdir}/gimp/%{api}/plug-ins >> %{buildroot}%{_libdir}/python%{pyver}/site-packages/gimp.pth
%endif

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f gimp20.lang
%doc AUTHORS NEWS README README.i18n docs/Wilber*
%config(noreplace) %{_sysconfdir}/gimp
%{_bindir}/gimp
%{_bindir}/gimp-%{abi}
%{_bindir}/gimp-console
%{_bindir}/gimp-console-%{abi}
%{_datadir}/applications/*
%{_datadir}/gimp
%dir %{_libdir}/gimp/%{api}
%dir %{_libdir}/gimp/%{api}/environ
%{_libdir}/gimp/%{api}/interpreters
%{_libdir}/gimp/%{api}/environ/default.env
%{_libdir}/gimp/%{api}/modules
%{_libdir}/gimp/%{api}/plug-ins
%exclude %{_libdir}/gimp/%{api}/plug-ins/*.py
%{_mandir}/man1/gimp-*
%{_mandir}/man1/gimp.*
%{_mandir}/man5/gimp*
%{_datadir}/icons/hicolor/*/apps/gimp.png
%{_datadir}/icons/hicolor/scalable/apps/gimp.svg

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
%{_libdir}/python%{pyver}/site-packages/*.pth
%endif

