%define	name	x2x
%define version 1.30
%define release %mkrel 0.beta.7

Summary:	Allows a mouse and a keyboard to control two displays
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://freshmeat.net/projects/%{name}/
Source0:	ftp://digital.com/pub/Digital/SRC/%{name}/%{name}-%{version}-beta.tar.bz2
Source1:	Makefile-%{name}.bz2
Patch0:		%{name}-1.30-c-fixes.patch.bz2
Patch1:		x2x-1.30beta-mdv-fix-str-fmt.patch
Group:		System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD
BuildRequires:	X11-devel imake
# for rman
BuildRequires:	xorg-x11

%description
x2x allows the keyboard and mouse on one ("from") X display to control 
another ("to") X display.

%prep
%setup -q -n %{name}-%{version}-beta
%patch0 -p1
%patch1 -p1 -b .strfmt
bzcat %{SOURCE1} > Makefile

%build
xmkmf
%make CFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG"

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -m644 %{name}.man -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.30-0.beta.7mdv2011.0
+ Revision: 615480
- the mass rebuild of 2010.1 packages

* Sat Dec 05 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 1.30-0.beta.6mdv2010.1
+ Revision: 473882
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.30-0.beta.4mdv2009.0
+ Revision: 168344
- fix no-buildroot-tag

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.30-0.beta.4mdv2008.1
+ Revision: 135580
- BR imake
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import x2x


* Thu Jan 19 2006 Michael Scherer <misc@mandriva.org> 1.30-0.beta.4mdk
- buildRequires rman, thanks ldb
- use %%mkrel 
- fix rpmlint about group

* Wed Jan 18 2006 Lenny Cartier <lenny@mandriva.com> 1.30-0.beta.3mdk
- fix x86_64 build

* Thu Jun 02 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.30-0.beta.2mdk
- Rebuild

* Sun Jan 04 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 1.30-0.beta.1mdk
- 1.30-beta
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- cosmetics
- regenerate P0

* Mon Feb 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.27-1mdk
- from Quel Qun <kelk1@hotmail.com> :
	- Mandrake rpm.
