Summary: A Tk toolkit extension, including widgets, geometry managers, etc.
Name: blt
Version: 2.4g
Release: 4
Copyright: MIT
Group: Development/Tools
Obsoletes: blt-devel
Source0: ftp://ftp.tcltk.org/pub/blt/BLT2.4g.tar.gz
Patch0: blt-2.4f-prefix.patch
Buildroot: /var/tmp/blt-root

%description
BLT is an extension to the Tk toolkit.  BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry
managers and miscellaneous other commands.  Note that you won't need to
do any patching of the Tcl or Tk source files to use BLT, but you
will need to have Tcl/Tk installed in order to use BLT.

If you are programming with the Tk toolkit, you should install BLT.
You will need to have Tcl/Tk installed.

%prep
%setup -q -n blt%{version}
%patch -b .prefix -p1

%build
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,sbin}
make exec_prefix=$RPM_BUILD_ROOT/usr prefix=$RPM_BUILD_ROOT/usr \
  scriptdir=$RPM_BUILD_ROOT/usr/lib/blt2.4 bare_prefix=/usr install
ln -sf libBLT.so.2.4 $RPM_BUILD_ROOT/usr/lib/libBLT.so
strip $RPM_BUILD_ROOT/usr/bin/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README html
/usr/bin/bltwish2.4
/usr/bin/bltwish
/usr/lib/libBLT.a
/usr/lib/libBLT.so.2.4
/usr/lib/libBLT.so
/usr/lib/blt2.4
/usr/include/blt.h
/usr/man/mann/BLT.n
/usr/man/mann/barchart.n
/usr/man/mann/bgexec.n
# bitmap.n is in tcl as well
#/usr/man/mann/bitmap.n
/usr/man/mann/bltdebug.n
/usr/man/mann/busy.n
/usr/man/mann/dragdrop.n
/usr/man/mann/eps.n
/usr/man/mann/graph.n
/usr/man/mann/htext.n
/usr/man/mann/hierbox.n
/usr/man/mann/spline.n
/usr/man/mann/stripchart.n
/usr/man/mann/table.n
# tabset.n is in itcl as well
#/usr/man/mann/tabset.n
/usr/man/mann/tile.n
/usr/man/mann/vector.n
# watch.n is in itcl as well
#/usr/man/mann/watch.n
/usr/man/mann/winop.n
/usr/man/mann/beep.n
/usr/man/mann/cutbuffer.n

%changelog
* Fri Apr 16 1999 Bill Nottingham <notting@redhat.com>
- obsolete blt-devel

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- remove watch.n, tabset.n (conflicts with itcl)

* Wed Mar 10 1999 Bill Nottingham <notting@redhat.com>
- update to 2.4g
- buildrooted

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- stripped binaries
