Summary:	A Tk toolkit extension, including widgets, geometry managers, etc.
Name:		blt
Version:	2.4g
Release:	5
Copyright:	MIT
Group:		Development/Tools
Obsoletes:	blt-devel
Source0:	ftp://ftp.tcltk.org/pub/blt/BLT%{version}.tar.gz
Patch0:		blt-prefix.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry
managers and miscellaneous other commands. Note that you won't need to do
any patching of the Tcl or Tk source files to use BLT, but you will need to
have Tcl/Tk installed in order to use BLT.

If you are programming with the Tk toolkit, you should install BLT.
You will need to have Tcl/Tk installed.

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

make exec_prefix=$RPM_BUILD_ROOT/usr prefix=$RPM_BUILD_ROOT/usr \
  scriptdir=$RPM_BUILD_ROOT/usr/lib/blt2.4 bare_prefix=/usr install

ln -sf libBLT.so.2.4 $RPM_BUILD_ROOT/usr/lib/libBLT.so

rm -f $RPM_BUILD_ROOT%{_mandir}/mann/{bitmap,tabset,watch}.n

strip $RPM_BUILD_ROOT/usr/bin/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/mann/*
	README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz html
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/lib*.so.*.*
/usr/lib/blt2.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/blt.h
%{_mandir}/mann/*

%files static
%attr(644,root,root) /usr/lib/lib*.a
