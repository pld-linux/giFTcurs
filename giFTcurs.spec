Summary:	ncurses-based FastTrack client
Summary(pl):	Klient FastTrack
Name:		giFTcurs
Version:	0.3.0.cvs20020206
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://prdownloads.sourceforge.net/giftcurs/%{name}-%{version}.tar.gz
URL:		http://giftcurs.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	giFT
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'giFTcurs' ncurses client for FastTrack network

%description -l pl
Klient sieci FastTrack


%prep
%setup -q -n giFTcurs-0.3.0

%build
automake --add-missing
autoconf
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
