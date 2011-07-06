Summary: Red Hat specific rpm configuration files
Name: redhat-rpm-config
Version: 9.0.3
Release: 25%{?dist}
# No version specified.
License: GPL+
Group: Development/System
Source: redhat-rpm-config-%{version}.tar.bz2
Patch0: redhat-rpm-config-9.0.3-fix-requires.patch
Patch1: limit-smp-16-threads.patch
Patch2: redhat-rpm-config-9.0.3-F-11-Architectures.patch
Patch3: redhat-rpm-config-9.0.3-F-11-StrongerHashes.patch
Patch4: redhat-rpm-config-9.0.3-F-12-Architectures.patch
Patch5: redhat-rpm-config-9.0.3-always_delete_buildroot_at_install.patch
Patch6: redhat-rpm-config-9.0.3-xz-payload.patch
Patch7: redhat-rpm-config-9.0.3-jars-with-spaces.patch
Patch8: redhat-rpm-config-9.0.3-brpssa-speedup.patch
Patch9: redhat-rpm-config-9.0.3-filtering-macros.patch 
Patch10: redhat-rpm-config-9.0.3-RHEL6-ksyms-updates.patch
Patch11: redhat-rpm-config-9.0.3-empty-jars.patch
Patch12: redhat-rpm-config-9.0.3-RHEL6-kmod-post-uninstall-add-target-cpu-to-depmod-fix.patch
Patch13: redhat-rpm-config-9.0.3-RHEL6-fix-buildreqs-in-kmodtool-for-brew.patch
Patch14: redhat-rpm-config-9.0.3-RHEL6-ksyms-updates2.patch
Patch15: redhat-rpm-config-9.0.3-RHEL6-kmodtool-fix-module-removal.patch
BuildArch: noarch
Requires: mktemp
BuildRoot: %{_tmppath}/%{name}-root

%description
Red Hat specific rpm configuration files.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p5
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%install
make DESTDIR=${RPM_BUILD_ROOT} install
find ${RPM_BUILD_ROOT} -name \*.orig -delete

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_prefix}/lib/rpm/redhat

%changelog
* Tue Aug 10 2010 Jon Masters <jcm@redhat.com> - 9.0.3-25
- Update the kmodtool and correct kmod removal to delete package-specific files
- Resolves: #622618.

* Wed Jul 28 2010 Jon Masters <jcm@redhat.com> - 9.0.3-24
- Update the kmodtool and the percent kernel_module_package macro in
  accordance with the upstream packaging standard.
- Resolves: #618518.

* Wed Jun 30 2010 Jon Masters <jcm@redhat.com> - 9.0.3-22
- Fix BuildRequires in kmodtool for use with internal tools.
- Resolves: #480415.

* Tue Jun 29 2010 Jon Masters <jcm@redhat.com> - 9.0.3-21
- Fix depmod call at kmod uninstall to find the right /lib/modules path.
- Resolves: #592215.

* Sun Mar 28 2010 Jon Masters <jcm@redhat.com> - 9.0.3-20
- updated RHEL6 kmod packaging macros.

* Fri Jan 22 2010 Panu Matilainen <pmatilai@redhat.com> - 9.0.3-19
- Dont try to repack empty JAR's (#547699)

* Tue Jan 12 2010 Jon Masters <jcm@redhat.com> - 9.0.3-18.10
- updated RHEL6 kmod packaging macros.

* Thu Nov 19 2009 Dennis Gregorovic <dgregor@redhat.com> - 9.0.3-18.1
- ksyms patch

* Mon Sep 28 2009 Bill Nottingham <notting@redhat.com>
- Drop xz compression level to 2

* Thu Sep 03 2009 Adam Jackson <ajax@redhat.com>
- Delete *.orig in %%install

* Thu Sep 03 2009 Paul Howarth <paul@city-fan.org> 9.0.3-17
- redhat-rpm-config-9.0.3-filtering-macros.patch: Rediff so we don't ship a .orig file
- add (empty) %%build section
- fix unescaped macros in changelog

* Tue Aug 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 9.0.3-16
- add the filtering framework approved by the FPC/FESCo. (#516240)

* Thu Aug 13 2009 Adam Jackson <ajax@redhat.com> 9.0.3-15
- redhat-rpm-config-9.0.4-brpssa-speedup.patch: When looking for static
  archives, only run file(1) on files named *.a. (#517101)

* Wed Aug 12 2009 Adam Jackson <ajax@redhat.com> 9.0.3-14
- redhat-rpm-config-9.0.3-jars-with-spaces.patch: Handle repacking jars
  whose filenames contain spaces. (#461854)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Bill Nottingham <notting@redhat.com> 9.0.3-12
- use XZ payload compression for binary packages

* Tue Jul 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 9.0.3-10
- always delete %%buildroot as first step of %%install (as long as %%buildroot is not /)

* Fri Jul 17 2009 Bill Nottingham <notting@redhat.com> 9.0.3-10
- apply fedora 12 default buildflags

* Wed Jun 03 2009 Adam Jackson <ajax@redhat.com> 9.0.3-9
- limit-smp-16-threads.patch: Rediff so we don't ship a .orig file (#500316)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Jon Masters <jcm@redhat.com> - 9.0.3-7
- Change default hashing algorithm in file digests to SHA-256
- Resolves: #485826.

* Tue Feb 17 2009 Dennis Gilmore <dennis@ausil.us> - 9.0.3-6
- add missing armv7l arch  
- set the default build arch to match fedora arm build target

* Mon Feb 16 2009 Dennis Gilmore <dennis@ausil.us> - 9.0.3-5
- apply fedora 11 default buildflags
- set 32 bit intel build arch to i586 on compatiable hardware
- set 32 bit sparc build arch to sparcv9 on compatiable hardware

* Mon Feb 16 2009 Dennis Gilmore <dennis@ausil.us> - 9.0.3-4
- limit _smp_flags to -j16

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 9.0.3-3
- fix license tag
- nuke ancient conflicts

* Mon Aug 11 2008 Panu Matilainen <pmatilai@redhat.com> - 9.0.3-2
- Unbreak find-requires (#443015)

* Tue May 06 2008 Jon Masters <jcm@redhat.com> - 9.0.3-1
- Ensure Java Jar files have readable files within.
- Remove overwritten config.guess|sub files (testing).
- Fix Fortran flags for building using _fmoddir.
- Pull in objdump fix to upstream find-requires.

* Thu Apr 03 2008 Jon Masters <jcm@redhat.com> - 9.0.2-1
- Remove smp dependencies
- Update config.guess|sub files
- Don't call find-requires.ksyms for kmod packages (kernel kABI scripts).

* Thu Jul 05 2007 Jesse Keating <jkeating@redhat.com> - 9.0.1-1
- Remove dist defines, fedora-release does that now
- Enable post-build buildroot checking by default

* Tue Jun 19 2007 Jeremy Katz <katzj@redhat.com> - 9.0.0-1
- use stock find-lang.sh (#213041)
- arm fixes (Lennert Buytenhek, #243523)
- allow jar repacking to be disabled (#219731)
- fix running dist.sh --fc (#223651)
- hardlink identical .pyc and .pyo files to save space (Ville Skyttä)
- fix TMPDIR usage (Matthew Miller, #235614)

* Tue Jun 19 2007 Jeremy Katz <katzj@redhat.com> - 8.1.0-1
- add modalias tags to kmod packages and other kmod changes (jcm)
- recompress jars to avoid multilib conflicts (bkonrath)

* Fri May 18 2007 Jesse Keating <jkeating@redhat.com> 8.0.45-16
- Update macros for F8
- hardcode dist in release string, as we provide it.  chicken/egg.

* Wed Apr 11 2007 Jon Masters <jcm@redhat.com> 8.0.45-15
- Add modalias tags to kernel module packages (kmods) for tracking.
- Further information is available at http://www.kerneldrivers.org/.

* Tue Apr 03 2007 Jon Masters <jcm@redhat.com> 8.0.45-14
- Rebased all previous patches (since java fix introduced offset).
- Added Fedora per-release macros to platforms section of macros.
  Further debate may see these move elsewhere in the ordering.

* Tue Mar 13 2007 Ben Konrath <bkonrath@redhat.com> 8.0.45-13
- Update brp-java-repack-jars to fix issue with tomcat. 

* Wed Oct 18 2006 Jon Masters <jcm@redhat.com> 8.0.45-12
- Synced kernel_module_package semantics with SuSE.
- Updated kmodtool.

* Tue Oct 17 2006 Jon Masters <jcm@redhat.com> 8.0.45-10
- Updated kernel_module_package.

* Mon Oct 16 2006 Jon Masters <jcm@redhat.com> 8.0.45-9
- Added kernel_module_package macro. Working on unified packaging.

* Thu Oct 12 2006 Jon Masters <jcm@redhat.com> 8.0.45-8
- Added patch for find-requires. Waiting on write access to public CVS.

* Tue Sep 12 2006 Deepak Bhole <dbhole@redhat.com> 8.0.45-6
- Fix brp-java-repack-jars to work with builddirs that aren't %%name-%%version

* Mon Sep 11 2006 Fernando Nasser <fnasser@redhat.com> - 8.0.45-5
- Fix order of tokens in find command (thanks mikeb@redhat.com)

* Thu Sep  7 2006 Ben Konrath <bkonrath@redhat.com> - 8.0.45-4
- Fix bug in repack jars script. 

* Wed Sep  6 2006 Jeremy Katz <katzj@redhat.com> - 8.0.45-3
- path fix

* Tue Sep  5 2006 Jeremy Katz <katzj@redhat.com> - 8.0.45-2
- Add script from Ben Konrath <bkonrath@redhat.com> to repack jars to 
  avoid multilib conflicts

* Sun Jul 30 2006 Jon Masters <jcm@redhat.com> - 8.0.45-1
- Fix inverted kernel test.

* Sun Jul 30 2006 Jon Masters <jcm@redhat.com> - 8.0.44-1
- Add a better check for a kernel vs. kmod.

* Thu Jun 15 2006 Jon Masters <jcm@redhat.com> - 8.0.43-1
- Workaround bug in find-requires/find-provides for kmods.

* Thu Jun 15 2006 Jon Masters <jcm@redhat.com> - 8.0.42-1
- Fix a typo in KMP find-requires.

* Tue Jun 13 2006 Jon Masters <jcm@redhat.com> - 8.0.41-1
- Add support for KMP Fedora Extras packaging.

* Fri Feb  3 2006 Jeremy Katz <katzj@redhat.com> - 8.0.40-1
- use -mtune=generic for x86 and x86_64

* Tue Aug 16 2005 Elliot Lee <sopwith@redhat.com> - 8.0.39-1
- Fix #165416

* Mon Aug 01 2005 Elliot Lee <sopwith@redhat.com> - 8.0.38-1
- Add -Wall into cflags

* Mon Aug 01 2005 Elliot Lee <sopwith@redhat.com> - 8.0.37-1
- Patch from Uli: enable stack protector, fix sparc & ppc cflags

* Thu Jun 16 2005 Elliot Lee <sopwith@redhat.com> - 8.0.36-1
- Fix the fix

* Wed Apr  6 2005 Elliot Lee <sopwith@redhat.com> - 8.0.35-1
- Fix #129025 (enable python byte compilation)

* Wed Mar 23 2005 Elliot Lee <sopwith@redhat.com> 8.0.34-1
- Bug fixes
- Cflags change by drepper

* Wed Feb 9 2005 Elliot Lee <sopwith@redhat.com> 8.0.33-1
- Change -D to -Wp,-D to make java happy
- Add -D_FORTIFY_SOURCE=2 to global cflags (as per Jakub & Arjan's request)

* Fri Oct  1 2004 Bill Nottingham <notting@redhat.com> 8.0.32-1
- allow all symbol versioning in find_requires - matches RPM internal
  behavior

* Mon Jun 28 2004 Elliot Lee <sopwith@redhat.com> 8.0.31-1
- Add ppc8[25]60 to rpmrc optflags

* Fri Jun 25 2004 Elliot Lee <sopwith@redhat.com> 8.0.29-1
- rpmrc patch from jakub to change optflags.

* Wed Sep 17 2003 Elliot Lee <sopwith@redhat.com> 8.0.28-1
- Change brp-compress to pass -n flag to gzip (per msw's request)

* Tue Jul 15 2003 Elliot Lee <sopwith@redhat.com> 8.0.27-1
- Fix broken configure macro find for config.guess/config.sub
- Put host/target/build back for now

* Mon Jul  7 2003 Jens Petersen <petersen@redhat.com> - 8.0.26-1
- preserve the vendor field when VENDOR not set
- put VENDOR in the final i386-libc line, not the tentative one

* Mon Jul  7 2003 Jens Petersen <petersen@redhat.com> - 8.0.25-1
- update config.{guess,sub} to 2003-06-17
- define VENDOR to be redhat only when /etc/redhat-release present
  [suggested by jbj]
- put VENDOR in vendor field in our config.guess file for
  ia64, ppc, ppc64, s390, s390x, x86_64 and elf32-i386 Linux
- drop the --host, --build, --target and --program-prefix configure options
  from %%configure, since this causes far too many problems

* Fri May  2 2003 Jens Petersen <petersen@redhat.com> - 8.0.24-3
- make config.{guess,sub} executable

* Thu May  1 2003 Jens Petersen <petersen@redhat.com> - 8.0.22-2
- add config.guess and config.sub (2003-02-22) with s390 patch on config.sub
- make %%configure use them

* Mon Mar 03 2003 Elliot Lee <sopwith@redhat.com>
- Unset $DISPLAY in macros

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com> 8.0.21-1
- Just turn on -g unconditionally for now

* Thu Feb 13 2003 Elliot Lee <sopwith@redhat.com> 8.0.20-1
- Reorganize rpmrc/macros to set cflags in a nicer manner.

* Wed Jan 22 2003 Elliot Lee <sopwith@redhat.com> 8.0.19-1
- Disable brp-implant-ident-static until it works everywhere

* Thu Jan 16 2003 Nalin Dahyabhai <nalin@redhat.com> 8.0.18-1
- add brp-implant-ident-static, which requires mktemp

* Thu Jan  9 2003 Bill Nottingham <notting@redhat.com> 8.0.17-1
- add brp-strip-static-archive from rpm-4.2-0.54

* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 8.0.16-1
- make -g in rpmrc conditional on debug_package

* Mon Dec 16 2002 Elliot Lee <sopwith@redhat.com> 8.0.15-1
- Rename -debug subpackages to -debuginfo

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 8.0.14-1
- tweak debug package stuff so that we are overloading %%install
  instead of %%post

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 8.0.13-1
- turn on internal rpm dep generation by default

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 8.0.12-1
- New release with debug packages on

* Tue Dec  3 2002 Bill Nottingham <notting@redhat.com> 8.0.8-1
- turn debug packages off
- override optflags with no -g

* Fri Nov 22 2002 Elliot Lee <sopwith@redhat.com> 8.0.7-1
- turn on debug packages

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 8.0.6-1
- Pass __strip and __objdump macros

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 8.0.5-1
- Update macros to specify find-provides/find-requires

* Thu Oct 31 2002 Elliot Lee <sopwith@redhat.com> 8.0.4-1
- Remove tracking dependency

* Wed Oct 16 2002 Phil Knirsch <pknirsch@redhat.com> 8.0.3-2
- Added fix for outdated config.[sub|guess] files in %%configure section

* Wed Oct 16 2002 Elliot Lee <sopwith@redhat.com> 8.0.3-1
- New release that blows up on unpackaged files and missing doc files.

* Thu Oct  3 2002 Jeremy Katz <katzj@redhat.com> 8.0.2
- don't redefine everything in macros, just what we need to

* Mon Sep 16 2002 Alexander Larsson <alexl@redhat.com> 8.0.1
- Add debug package support to %%__spec_install_post

* Tue Sep  3 2002 Bill Nottingham <notting@redhat.com> 8.0-1
- bump version

* Wed Aug 28 2002 Elliot Lee <sopwith@redhat.com> 7.3.94-1
- Update macrofiles

* Wed Jul 31 2002 Elliot Lee <sopwith@redhat.com> 7.3.93-1
- Add _unpackaged_files_terminate_build and 
_missing_doc_files_terminate_build to macros

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-6
- find-lang.sh fix from 67368
- find-requires fix from 67325

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-5
- Add /etc/rpm/macros back to make #67951 go away

* Wed Jun 26 2002 Jens Petersen <petersen@redhat.com> 7.3.92-4
- fix %%configure targeting for autoconf-2.5x (#58468)
- include ~/.rpmmacros in macrofiles file path again

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 7.3.92-3
- automated rebuild

* Fri Jun 21 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-2
- Don't define _arch

* Thu Jun 20 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-1
- find-lang error detection from Havoc

* Wed Jun 12 2002 Elliot Lee <sopwith@redhat.com> 7.3.91-1
- Update

* Sun Jun  9 2002 Jeff Johnson <jbj@redhat.com>
- create.
