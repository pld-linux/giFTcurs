Summary:	ncurses-based giFT client
Summary(pl):	Klient giFT
Name:		giFTcurs
Version:	0.4.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://prdownloads.sourceforge.net/giftcurs/%{name}-%{version}.tar.gz
URL:		http://giftcurs.sourceforge.net/
#wywala "jakie¶" b³êdy przy automake
#BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncurses client for giFT (OpenFT network).

%description -l pl
Klient giFT (sieci OpenFT), napisany w ncurses.


%prep
%setup

%build
#wywala "jakie¶" b³êdy przy automake
#automake --add-missing
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README AUTHORS COPYING ChangeLog INSTALL NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
