Summary:	A Tk toolkit extension, including widgets, geometry managers, etc
Summary(es.UTF-8):	Componentes (widgets) y comandos extras para aplicaciones Tk
Summary(pl.UTF-8):	Rozszerzenie Tk umożliwiające operowanie na kontrolkach i wiele innych
Summary(pt_BR.UTF-8):	Componentes (widgets) e comandos extras para aplicações Tk
Summary(ru.UTF-8):	Расширение набора Tk, включая графические примитивы, менеджеры геометрии и т.д
Summary(uk.UTF-8):	Розширення набору Tk, включаючи графічні примітиви, менеджери геометрії і т.і
Name:		blt
Version:	2.4z
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/blt/BLT%{version}.tar.gz
# Source0-md5:	aa2ed73080f3005d9c2a3b5e57ab1eff
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-excl.patch
Patch3:		%{name}-acfix.patch
Patch4:		%{name}-nolibnsl.patch
Patch5:		%{name}-tcltk84.patch
Patch6:		%{name}-norpath.patch
Patch7:		%{name}-tcl85.patch
Patch8:		%{name}-decl.patch
Patch9:		%{name}-link.patch
Patch10:	%{name}-64bit.patch
URL:		http://blt.sourceforge.net/
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

%description -l es.UTF-8
BLT ofrece componentes (widgets) y comandos extras para programas Tk.
Incluye componentes gráficos, administración de geometría de tablas y
folders.

%description -l pl.UTF-8
BLT jest rozszerzeniem Tk. Najbardziej użyteczną funkcją BLT jest
rozszerzenie Tk o większą ilość kontrolek; oferuje również więcej
funkcji zarządzania geometrią i innych poleceń. Aby używać BLT nie
trzeba łatać plików źródłowych Tcl ani Tk, trzeba jednak mieć
zainstalowanego Tcl/Tk. Jeśli programuje się w Tcl/Tk, lepiej
zainstalować BLT. Trzeba również zainstalować Tcl/Tk.

%description -l pt_BR.UTF-8
O BLT fornece componentes (widgets) e comandos extras para programas
Tk. Ele inclui componentes gráficos, gerenciamento de geometria de
tabelas e folders.

%description -l ru.UTF-8
BLT - это расширение набора Tk. Наиболее ценной особенностью BLT
является предоставление бОльшего набора примитивов для Tk, но он также
предоставляет больше менеджеров геометрии и прочих команд. Следует
отметить, что вам не надо изменять исходных текстов Tcl или Tk для
того, чтобы использовать BLT, но вам необходимо установить Tcl/Tk для
использования BLT.

%description -l uk.UTF-8
BLT - це розширення набору Tk. Найбільш цінною особливістю BLT є
надання більшого набору примітивів для Tk, але він також надає більше
менджерів геометрії та інших команд. Слід зазначити, що вам не треба
змінювати вихідних текстів Tcl або Tk для того, щоб використовувати
BLT, але вам необхідно встановити Tcl/Tk для використання BLT.

%package devel
Summary:	BLT development package
Summary(pl.UTF-8):	Pakiet dla programistów BLT
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description devel
BLT header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe BLT.

%package static
Summary:	BLT static libraries
Summary(pl.UTF-8):	Biblioteki statyczne BLT
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description static
BLT static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne BLT.

%package demos
Summary:	BLT demos and examples
Summary(pl.UTF-8):	Dema i przykłady do BLT
Summary(pt_BR.UTF-8):	Programas que demonstram as características do BLT
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description demos
BLT demos and examples.

%description demos -l pl.UTF-8
Programy demonstracyjne i przykładowe do BLT.

%description demos -l pt_BR.UTF-8
Programas que demonstram as características do BLT.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
cp -f /usr/share/automake/config.* cf
%{__autoconf}
%configure \
	--with-tcllibs=%{_libdir} \
	--with-tklibs=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_examplesdir}/%{name}-%{version},%{_mandir}}

%{__make} -j1 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

ln -sf libBLT24.so $RPM_BUILD_ROOT%{_libdir}/libBLT.so
ln -sf libBLTlite24.so $RPM_BUILD_ROOT%{_libdir}/libBLTlite.so

# use dynamically linked binaries
mv -f $RPM_BUILD_ROOT%{_bindir}/bltsh{24,}
mv -f $RPM_BUILD_ROOT%{_bindir}/bltwish{24,}

# bitmap.n is provided by tk-devel
rm -f $RPM_BUILD_ROOT%{_mandir}/mann/bitmap.n

mv -f $RPM_BUILD_ROOT%{_ulibdir}/blt2.4/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -rf examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
