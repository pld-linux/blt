Summary:	A Tk toolkit extension, including widgets, geometry managers, etc
Summary(es):	Componentes (widgets) y comandos extras para aplicaciones tk
Summary(pl):	Rozszerzenie Tk umo�liwiaj�ce operowanie na kontrolkach i wiele innych
Summary(pt_BR):	Componentes (widgets) e comandos extras para aplica��es tk
Summary(ru):	���������� ������ tk, ������� ����������� ���������, ��������� ��������� � �.�
Summary(uk):	���������� ������ tk, ��������� ���Ʀ�Φ ���ͦ����, ��������� ������Ҧ� � �.�
Name:		blt
Version:	2.4u
Release:	9
License:	MIT
Group:		Development/Tools
Source0:	ftp://ftp.scriptics.com/pub/tcl/blt/BLT%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-excl.patch
Patch3:		%{name}-acfix.patch
Patch4:		%{name}-nolibnsl.patch
URL:		http://www.tcltk.com/blt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BLT is an extension to the Tk toolkit. BLT's most useful feature is
the provision of more widgets for Tk, but it also provides more
geometry managers and miscellaneous other commands. Note that you
won't need to do any patching of the Tcl or Tk source files to use
BLT, but you will need to have Tcl/Tk installed in order to use BLT.
If you are programming with the Tk toolkit, you should install BLT.
You will need to have Tcl/Tk installed.

%description -l es
BLT ofrece componentes (widgets) y comandos extras para programas tk.
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
tk. Ele inclui componentes gr�ficos, gerenciamento de geometria de
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
Requires:	%{name} = %{version}

%description devel
BLT header files.

%description devel -l pl
Pliki nag��wkowe BLT.

%package static
Summary:	BLT static libraries
Summary(pl):	Biblioteki statyczne BLT
Group:		Development/Tools
Requires:	%{name}-devel = %{version}

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
Requires:	%{name} = %{version}

%description demos
BLT demos and examples.

%description demos -l es
BLT Demonstrations.

%description demos -l pl
Programy demonstracyjne i przyk�adowe do BLT.

%description demos -l pt_BR
Programas que demonstram as caracter�sticas do BLT.

%prep
%setup -q -n blt%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.* cf
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS PROBLEMS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*24.so
%{_libdir}/blt2.4

%files devel
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_libdir}/lib*[a-zA-Z].so
%{_includedir}/blt*.h
%{_mandir}/mann/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
