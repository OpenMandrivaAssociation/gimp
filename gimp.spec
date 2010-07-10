%define name gimp
%define version 2.6.9
%define release %mkrel 1
%define lib_major 0

# optional compile flags
%define enable_python 1
%{?_without_python: %global enable_python 0}

%define enable_lzw 0
%{?_with_lzw: %global enable_lzw 1}

%define req_gtk_version 2.12.1

%define api_version 2.0
%define abi_version 2.6
%define libname	%mklibname %{name} %{api_version}_%{lib_major}
%define devlibname	%mklibname -d %{name}%{api_version}

Summary:	The GNU Image Manipulation Program
Name:		%name
Epoch:		1
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphics
URL:		http://www.gimp.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source0:	ftp://ftp.gimp.org/pub/gimp/v%{abi_version}/gimp-%version.tar.bz2
Source1:	ftp://ftp.gimp.org/pub/gimp/v%{abi_version}/gimp-%version.tar.bz2.md5
Source13:	gimp-scripting-sample.pl
Patch0: gimp-2.6.4-fix-str-fmt.patch
Patch1: gimp-2.6.4-fix-linking.patch
#gw fix name in desktop file and disable startup notification
Patch6:         gimp-2.5.1-desktopentry.patch
BuildRequires:  libxfixes-devel
BuildRequires:	gegl-devel >= 0.0.18
BuildRequires:	imagemagick
BuildRequires:	aalib-devel
BuildRequires:	gtk-doc >= 1.11-3mdv
BuildRequires:  libexif-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libgtk+2.0-devel >= %{req_gtk_version}
BuildRequires:	libgnomeui2-devel
BuildRequires:	libalsa-devel
%if %{mdkversion} >= 200800
BuildRequires:	libpoppler-glib-devel >= 0.4.1
%endif
BuildRequires:	libmng-devel
BuildRequires: 	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	perl
BuildRequires:	xpm-devel
BuildRequires:  librsvg-devel >= 2.14.0
BuildRequires:	libxmu-devel
BuildRequires:	intltool 
# mail plugin
BuildRequires:	sendmail-command
# help browser
BuildRequires:	libwebkitgtk-devel
# print plugin
#BuildRequires:	libgimpprint-devel >= 4.2.0
# python plugin
%if %enable_python
BuildRequires:	pygtk2.0-devel >= 2.10.4
BuildRequires:	python-devel
%endif
BuildRequires:  automake
BuildRequires:  lcms-devel
BuildRequires:  libwmf-devel >= 0.2.8
BuildRequires:  libhal-devel
BuildRequires:  libxext-devel
BuildRequires:  desktop-file-utils
%if %{mdkversion} <= 200800
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%endif
Provides: gimp1_3 gimp2_0 gimp2_2 gimp2.6
Obsoletes: gimp1_3 gimp2_0 gimp2_2 gimp2.6
# workaround libgimp not bumping its major on API/ABI changes:
Requires:	%{libname} = %epoch:%{version}
Requires(post):  desktop-file-utils
Requires(postun):  desktop-file-utils
Conflicts:	perl-Gimp < 2.2
Conflicts:	gutenprint-gimp2 < 5.0.1
Suggests: gimp-help-2

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

%package -n %{devlibname}
Summary:	GIMP plugin and extension development kit
Group:		Development/GNOME and GTK+
Requires:	libgtk+2.0-devel >= %{req_gtk_version}
Epoch:		1
License:	LGPLv2+
Requires:	%{libname} = %epoch:%{version}
Provides:	gimp-devel = %{version}-%{release}
Provides:	gimp2.6-devel = %{version}-%{release}
Provides:	libgimp-devel = %{version}-%{release}

%description -n %{devlibname}
Static libraries and header files for writing GIMP plugins and extensions.

%package -n %libname
Summary:	GIMP libraries
Group:		System/Libraries
Epoch:		1
License:	LGPLv2+
Provides:	libgimp%{api_version} = %{version}-%{release}
Obsoletes:	%mklibname gimp 2.6_2.0_0

%description -n %libname
This is the library that provides core GIMP functionality.
It enable other programs to use GIMP's features but is mainly intended
to be used by the GIMP and its "external" plugins.

%package python
Summary:	GIMP python extension
Group:		Graphics
Epoch:		1
Requires:	pygtk2.0
Obsoletes: gimp1_3-python, gimp2_0-python, gimp2_2-python

%description python
This package contains the python modules for GIMP, which act as a
wrapper to libgimp allowing the writing of plug-ins for Gimp.
This is similar to script-fu, except that you can use the full set
of Python extension modules from the plug-in, and you write plug-in
in python instead of in scheme.

%prep
%setup -q -n gimp-%version
%patch0 -p1 -b .fix-str-fmt
%patch1 -p1 -b .fix-linking
%patch6 -p1 -b .desktopentry

#needed by patch1
autoreconf -fi -I m4macros

%build

%configure2_5x --enable-default-binary=yes \
	--enable-mp=yes		\
%if %enable_python
	--enable-python=yes	\
%else
	--enable-python=no	\
%endif
%if %enable_lzw
	--with-gif-compression=lzw	\
%else
	--with-gif-compression=rle	\
%endif
	--enable-gtk-doc=yes	

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

#clean unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{api_version}/*/*.a
find %buildroot -name \*la|xargs chmod 644

# workaround broken help system                                                                               
HELP_DIR=$RPM_BUILD_ROOT%_datadir/gimp/%api_version/help/C
[[ -d $HELP_DIR ]] || mkdir -p $HELP_DIR
HELP_IDX=$HELP_DIR/introduction.html
echo -e '<HTML><HEAD><TITLE>GIMP Base Library</HEAD>\n<BODY><UL>' > $HELP_IDX

/bin/ls $RPM_BUILD_ROOT%_datadir/gtk-doc/html/*/index.html | sed -e "s@$RPM_BUILD_ROOT@@g" >> $HELP_IDX
perl -pi -e 's!(.*/html/)([^/]*)(/index.html)!<LI><A HREF="\1\2\3">\2</A>!g' $HELP_IDX

echo '</UL></BODY></HTML>' >> $HELP_IDX

%find_lang gimp20 --all-name

%if %enable_python
chmod 755 %buildroot%_libdir/gimp/%{api_version}/plug-ins/*.py
mkdir -p %{buildroot}%{_libdir}/python%{pyver}/site-packages
echo %_libdir/gimp/%{api_version}/python > %{buildroot}%{_libdir}/python%{pyver}/site-packages/gimp.pth
echo %_libdir/gimp/%{api_version}/plug-ins >> %{buildroot}%{_libdir}/python%{pyver}/site-packages/gimp.pth
%endif

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_desktop_database
%update_icon_cache hicolor
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_desktop_database
%clean_icon_cache hicolor
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f gimp20.lang
%defattr(-,root,root,0755)
%{_bindir}/gimp
%{_bindir}/gimp-%abi_version
%{_bindir}/gimp-console
%{_bindir}/gimp-console-%abi_version
%{_datadir}/applications/*
%{_datadir}/gimp
%dir %{_libdir}/gimp/%{api_version}
%dir %{_libdir}/gimp/%{api_version}/environ
%{_libdir}/gimp/%{api_version}/interpreters
%{_libdir}/gimp/%{api_version}/environ/default.env
%{_libdir}/gimp/%{api_version}/modules
%{_libdir}/gimp/%{api_version}/plug-ins
%exclude %{_libdir}/gimp/%{api_version}/plug-ins/*.py
%{_mandir}/man1/gimp*
%{_mandir}/man5/gimp*
%_datadir/icons/hicolor/*/apps/gimp.png
%_datadir/icons/hicolor/scalable/apps/gimp.svg
%config(noreplace) %{_sysconfdir}/gimp

%doc AUTHORS NEWS README README.i18n docs/Wilber*

%files -n %{devlibname}
%defattr(-,root,root,0755)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/gimptool-*
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/gimptool-*

%files -n %libname
%defattr(-,root,root,755)
# explicitly list all libs to avoid old libtool issue
%{_libdir}/libgimpconfig-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimp-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpthumb-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpbase-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpcolor-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpmath-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpmodule-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpui-%{api_version}.so.%{lib_major}*
%{_libdir}/libgimpwidgets-%{api_version}.so.%{lib_major}*

%if %enable_python
%files python
%defattr(-,root,root,755)
%{_libdir}/gimp/%{api_version}/environ/pygimp.env
%{_libdir}/gimp/%{api_version}/python
%{_libdir}/gimp/%{api_version}/plug-ins/*.py
%{_libdir}/python%{pyver}/site-packages/*.pth
%endif
