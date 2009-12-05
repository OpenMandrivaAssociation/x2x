%define	name	x2x
%define version 1.30
%define release %mkrel 0.beta.6

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

