Summary:	A Tk toolkit extension, including widgets, geometry managers, etc
Summary(pl):	Rozszerzenie Tk umo¿liwiajace operowanie na kontrolkach i wiele innych
Name:		blt
Version:	2.4u
Release:	5
License:	MIT
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://tcltk.sourceforge.net/pub/tcltk/blt/BLT%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-excl.patch
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BLT is an extension to the Tk toolkit. BLT's most useful feature is
the provision of more widgets for Tk, but it also provides more
geometry managers and miscellaneous other commands. Note that you
won't need to do any patching of the Tcl or Tk source files to use
BLT, but you will need to have Tcl/Tk installed in order to use BLT.
If you are programming with the Tk toolkit, you should install BLT.
You will need to have Tcl/Tk installed.

%description -l pl
BLT jest rozszerzeniem Tk. Najbardziej u¿yteczn± funkcj± BLT jest
dostarczenie Tk wiêkszej ilo¶ci widgetów; oferuje równie¿ wiêcej
mened¿erów geometrii i innych poleceñ. Aby u¿ywaæ BLT nie trzeba ³ataæ
plików ¼ród³owych Tcl ani Tk, trzeba jednak mieæ zainstalowanego
Tcl/Tk. Je¶li programuje siê w Tcl/tk, nale¿y zainstalowaæ BLT. Trzeba
równie¿ zainstalowaæ Tcl/Tk.

%package devel
Summary:	BLT development package
Summary(pl):	Pakiet dla programistów BLT
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Requires:	%{name} = %{version}

%description devel
BLT header files.

%description devel -l pl
Pliki nag³ówkowe BLT.

%package static
Summary:	BLT static libraries
Summary(pl):	Biblioteki statyczne BLT
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Requires:	%{name}-devel = %{version}

%description static
BLT static libraries.

%description static -l pl
Biblioteki statyczne BLT.

%package demos
Summary:	BLT demos and examples
Summary(pl):	Dema i przyk³ady do BLT
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Requires:	%{name} = %{version}

%description demos
BLT demos and examples.

%description demos -l pl
Programy demonstracyjne i przyk³adowe do BLT.

%prep
%setup -q -n blt%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf libBLT24.so $RPM_BUILD_ROOT%{_libdir}/libBLT.so
ln -sf libBLTlite24.so $RPM_BUILD_ROOT%{_libdir}/libBLTlite.so

# use dynamically linked binaries
mv -f $RPM_BUILD_ROOT%{_bindir}/bltsh24 $RPM_BUILD_ROOT%{_bindir}/bltsh
mv -f $RPM_BUILD_ROOT%{_bindir}/bltwish24 $RPM_BUILD_ROOT%{_bindir}/bltwish

# bitmap.n is provided by tk-devel
rm -f $RPM_BUILD_ROOT%{_mandir}/mann/bitmap.n

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
mv -f $RPM_BUILD_ROOT%{_libdir}/blt2.4/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -rf examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

rm -f html/Makefile* $RPM_BUILD_ROOT%{_libdir}/blt2.4/{NEWS,README,PROBLEMS}

gzip -9nf README NEWS PROBLEMS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*24.so
%{_libdir}/blt2.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*[a-zA-Z].so
%doc *.gz html
%{_includedir}/blt.h
%{_mandir}/mann/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
