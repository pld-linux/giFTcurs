Summary:	ncurses-based giFT client
Summary(pl):	Klient giFT
Name:		giFTcurs
Version:	0.5.7
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/giftcurs/%{name}-%{version}.tar.gz
Patch0:		%{name}-home_etc.patch
# Source0-md5:	b9a30012f1083a99d5f34d384fa5ea0d
URL:		http://giftcurs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncurses client for giFT (OpenFT network).

%description -l pl
Klient giFT (sieci OpenFT), napisany w ncurses.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
