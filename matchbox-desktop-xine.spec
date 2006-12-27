Summary:	Movie and music player for Matchbox desktop
Summary(pl):	Odtwarzacz filmów i muzyki dla ¶rodowiska Matchbox
Name:		matchbox-desktop-xine
Version:	0.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/mb-desktop-xine/%{version}/mb-desktop-xine-%{version}.tar.bz2
# Source0-md5:	3805f463cbd1817c75fed5f9c4cd2f8b
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	libmatchbox-devel >= 1.1
BuildRequires:	matchbox-desktop-devel >= 0.8
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel >= 1:1.0.0
Requires:	libmatchbox >= 1.1
Requires:	matchbox-desktop >= 0.8
Requires:	xine-lib >= 1:1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a matchbox-desktop plugin that allows you to browse and play
movies and music.

%description -l pl
Wtyczka matchbox-desktop pozwalaj±ca na przegl±danie i odtwarzanie
filmów i muzyki.

%prep
%setup -q -n mb-desktop-xine-%{version}

%build
%configure \
	--disable-static
%{__make} \
	libdir=%{_libdir}/matchbox/desktop

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}/matchbox/desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/matchbox/desktop/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/matchbox/desktop/xinebrowser.so
%{_pixmapsdir}/*.png
%dir %{_datadir}/themes/mbmediabox
%{_datadir}/themes/mbmediabox/matchbox
