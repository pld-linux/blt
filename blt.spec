Summary:	A Tk toolkit extension, including widgets, geometry managers, etc.
Name:		blt
Version:	2.4q
Release:	1
License:	MIT
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Obsoletes:	blt-devel
Source0:	ftp://ftp.tcltk.com/aa004735/pub/blt/BLT%{version}.tar.gz
Patch0:		blt-prefix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry
managers and miscellaneous other commands. Note that you won't need to do
any patching of the Tcl or Tk source files to use BLT, but you will need to
have Tcl/Tk installed in order to use BLT.  If you are programming with the
Tk toolkit, you should install BLT. You will need to have Tcl/Tk installed.

%description -l pl
BLT jest rozszerzeniem Tk. Najbardziej u¿yteczn± funkcj± BLT jest
dostarczenie Tk wiêkszej ilo¶ci widgetów; oferuje równie¿ wiêcej mened¿erów
geometrii i innych poleceñ. Aby u¿ywaæ BLT nie trzeba ³ataæ plików
¼ród³owych Tcl ani Tk, trzeba jednak mieæ zainstalowanego Tcl/Tk. Je¶li
programuje siê w Tcl/tk, nale¿y zainstalowaæ BLT. Trzeba równie¿
zainstalowaæ Tcl/Tk.

%package devel

%package static

%prep
%setup -q -n blt%{version}
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,sbin}

make install \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	scriptdir=$RPM_BUILD_ROOT%{_libdir}/blt2.4 \
	bare_prefix=%{_prefix}

ln -sf libBLT.so.2.4 $RPM_BUILD_ROOT%{_libdir}/libBLT.so

rm -f $RPM_BUILD_ROOT%{_mandir}/mann/{bitmap,tabset,watch}.n

strip $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/mann/*
	README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/blt2.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/blt.h
%{_mandir}/mann/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
