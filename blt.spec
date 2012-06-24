Summary:	A Tk toolkit extension, including widgets, geometry managers, etc
Summary(es):	Componentes (widgets) y comandos extras para aplicaciones Tk
Summary(pl):	Rozszerzenie Tk umo�liwiaj�ce operowanie na kontrolkach i wiele innych
Summary(pt_BR):	Componentes (widgets) e comandos extras para aplica��es Tk
Summary(ru):	���������� ������ Tk, ������� ����������� ���������, ��������� ��������� � �.�
Summary(uk):	���������� ������ Tk, ��������� ���Ʀ�Φ ���ͦ����, ��������� ������Ҧ� � �.�
Name:		blt
Version:	2.4u
Release:	14
License:	MIT
Group:		Development/Tools
Source0:	ftp://ftp.scriptics.com/pub/tcl/blt/BLT%{version}.tar.gz
# Source0-md5:	bad9f33789a6aac390cebba819ee6b38
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-excl.patch
Patch3:		%{name}-acfix.patch
Patch4:		%{name}-nolibnsl.patch
Patch5:		%{name}-tcltk84.patch
Patch6:		%{name}-norpath.patch
URL:		http://incrtcl.sourceforge.net/blt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.4.6
BuildRequires:	tk-devel >= 8.4.6
Requires:	tcl >= 8.4.6
Requires:	tk >= 8.4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
BLT is an extension to the Tk toolkit. BLT's most useful feature is
the provision of more widgets for Tk, but it also provides more
geometry managers and miscellaneous other commands. Note that you
won't need to do any patching of the Tcl or Tk source files to use
BLT, but you will need to have Tcl/Tk installed in order to use BLT.
If you are programming with the Tk toolkit, you should install BLT.
You will need to have Tcl/Tk installed.

%description -l es
BLT ofrece componentes (widgets) y comandos extras para programas Tk.
Incluye componentes gr�ficos, administraci�n de geometr�a de tablas y
folders.

%description -l pl
BLT jest rozszerzeniem Tk. Najbardziej u�yteczn� funkcj� BLT jest
rozszerzenie Tk o wi�ksz� ilo�� kontrolek; oferuje r�wnie� wi�cej
funkcji zarz�dzania geometri� i innych polece�. Aby u�ywa� BLT nie
trzeba �ata� plik�w �r�d�owych Tcl ani Tk, trzeba jednak mie�
zainstalowanego Tcl/Tk. Je�li programuje si� w Tcl/Tk, lepiej
zainstalowa� BLT. Trzeba r�wnie� zainstalowa� Tcl/Tk.

%description -l pt_BR
O BLT fornece componentes (widgets) e comandos extras para programas
Tk. Ele inclui componentes gr�ficos, gerenciamento de geometria de
tabelas e folders.

%description -l ru
BLT - ��� ���������� ������ Tk. �������� ������ ������������ BLT
�������� �������������� �������� ������ ���������� ��� Tk, �� �� �����
������������� ������ ���������� ��������� � ������ ������. �������
��������, ��� ��� �� ���� �������� �������� ������� Tcl ��� Tk ���
����, ����� ������������ BLT, �� ��� ���������� ���������� Tcl/Tk ���
������������� BLT.

%description -l uk
BLT - �� ���������� ������ Tk. ���¦��� æ���� ������צ��� BLT �
������� ¦������ ������ ���ͦ��צ� ��� Tk, ��� צ� ����� ����� ¦����
������Ҧ� ������Ҧ� �� ����� ������. �̦� ���������, �� ��� �� �����
�ͦ������ ��Ȧ���� ����Ԧ� Tcl ��� Tk ��� ����, ��� ���������������
BLT, ��� ��� ����Ȧ��� ���������� Tcl/Tk ��� ������������ BLT.

%package devel
Summary:	BLT development package
Summary(pl):	Pakiet dla programist�w BLT
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description devel
BLT header files.

%description devel -l pl
Pliki nag��wkowe BLT.

%package static
Summary:	BLT static libraries
Summary(pl):	Biblioteki statyczne BLT
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description static
BLT static libraries.

%description static -l pl
Biblioteki statyczne BLT.

%package demos
Summary:	BLT demos and examples
Summary(pl):	Dema i przyk�ady do BLT
Summary(pt_BR):	Programas que demonstram as caracter�sticas do BLT
Summary(es):	BLT Demonstrations
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description demos
BLT demos and examples.

%description demos -l es
BLT Demonstrations.

%description demos -l pl
Programy demonstracyjne i przyk�adowe do BLT.

%description demos -l pt_BR
Programas que demonstram as caracter�sticas do BLT.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
cp -f /usr/share/automake/config.* cf
%{__autoconf}
%configure \
	--with-tcllibs=%{_libdir} \
	--with-tklibs=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_examplesdir}/%{name}-%{release}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

ln -sf libBLT24.so $RPM_BUILD_ROOT%{_libdir}/libBLT.so
ln -sf libBLTlite24.so $RPM_BUILD_ROOT%{_libdir}/libBLTlite.so

# use dynamically linked binaries
mv -f $RPM_BUILD_ROOT%{_bindir}/bltsh24 $RPM_BUILD_ROOT%{_bindir}/bltsh
mv -f $RPM_BUILD_ROOT%{_bindir}/bltwish24 $RPM_BUILD_ROOT%{_bindir}/bltwish

# bitmap.n is provided by tk-devel
rm -f $RPM_BUILD_ROOT%{_mandir}/mann/bitmap.n

mv -f $RPM_BUILD_ROOT%{_ulibdir}/blt2.4/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{release}
cp -rf examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{release}

rm -f html/Makefile* $RPM_BUILD_ROOT%{_ulibdir}/blt2.4/{NEWS,README,PROBLEMS}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS PROBLEMS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libBLT*24.so
%{_ulibdir}/blt2.4

%files devel
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_libdir}/libBLT*[A-Za-z].so
%{_includedir}/blt*.h
%{_mandir}/mann/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{release}
