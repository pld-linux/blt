Summary:	A Tk toolkit extension, including widgets, geometry managers, etc
Summary(es):	Componentes (widgets) y comandos extras para aplicaciones tk
Summary(pl):	Rozszerzenie Tk umo©liwiajace operowanie na kontrolkach i wiele innych
Summary(pt_BR):	Componentes (widgets) e comandos extras para aplicaГУes tk
Summary(ru):	Расширение набора tk, включая графические примитивы, менеджеры геометрии и т.д
Summary(uk):	Розширення набору tk, включаючи граф╕чн╕ прим╕тиви, менеджери геометр╕╖ ╕ т.╕
Name:		blt
Version:	2.4u
Release:	8
License:	MIT
Group:		Development/Tools
Source0:	ftp://tcltk.sourceforge.net/pub/tcltk/blt/BLT%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-excl.patch
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
#BuildRequires:	automake
#BuildRequires:	autoconf
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
Incluye componentes grАficos, administraciСn de geometrМa de tablas y
folders.

%description -l pl
BLT jest rozszerzeniem Tk. Najbardziej u©yteczn╠ funkcj╠ BLT jest
rozszerzenie Tk o wiЙksz╠ ilo╤Ф kontrolek; oferuje rСwnie© wiЙcej
funkcji zarz╠dzania geometri╠ i innych poleceЯ. Aby u©ywaФ BLT nie
trzeba ЁataФ plikСw ╪rСdЁowych Tcl ani Tk, trzeba jednak mieФ
zainstalowanego Tcl/Tk. Je╤li programuje siЙ w Tcl/Tk, nale©y
zainstalowaФ BLT. Trzeba rСwnie© zainstalowaФ Tcl/Tk.

%description -l pt_BR
O BLT fornece componentes (widgets) e comandos extras para programas
tk. Ele inclui componentes grАficos, gerenciamento de geometria de
tabelas e folders.

%description -l ru
BLT - это расширение набора Tk. Наиболее ценной особенностью BLT
является предоставление бОльшего набора примитивов для Tk, но он также
предоставляет больше менеджеров геометрии и прочих команд. Следует
отметить, что вам не надо изменять исходных текстов Tcl или Tk для
того, чтобы использовать BLT, но вам необходимо установить Tcl/Tk для
использования BLT.

%description -l uk
BLT - це розширення набору Tk. Найб╕льш ц╕нною особлив╕стю BLT ╓
надання б╕льшого набору прим╕тив╕в для Tk, але в╕н також нада╓ б╕льше
менджер╕в геометр╕╖ та ╕нших команд. Сл╕д зазначити, що вам не треба
зм╕нювати вих╕дних текст╕в Tcl або Tk для того, щоб використовувати
BLT, але вам необх╕дно встановити Tcl/Tk для використання BLT.

%package devel
Summary:	BLT development package
Summary(pl):	Pakiet dla programistСw BLT
Group:		Development/Tools
Requires:	%{name} = %{version}

%description devel
BLT header files.

%description devel -l pl
Pliki nagЁСwkowe BLT.

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
Summary(pl):	Dema i przykЁady do BLT
Summary(pt_BR):	Programas que demonstram as caracterМsticas do BLT
Summary(es):	BLT Demonstrations
Group:		Development/Tools
Requires:	%{name} = %{version}

%description demos
BLT demos and examples.

%description demos -l es
BLT Demonstrations.

%description demos -l pl
Programy demonstracyjne i przykЁadowe do BLT.

%description demos -l pt_BR
Programas que demonstram as caracterМsticas do BLT.

%prep
%setup -q -n blt%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#aclocal
#%{__autoconf}
%configure2_13
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
%doc README NEWS PROBLEMS html
%attr(755,root,root) %{_libdir}/lib*[a-zA-Z].so
%{_includedir}/blt.h
%{_mandir}/mann/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
