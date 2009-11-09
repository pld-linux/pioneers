# TODO
# - add init file for server
Summary:	Pioneers - emulation of the board game "The Settlers of Catan"
Summary(pl.UTF-8):	Pioneers - emulacja planszowej gry "Osadnicy z Catanu"
Name:		pioneers
Version:	0.12.3
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/pio/%{name}-%{version}.tar.gz
# Source0-md5:	459e82043fd8e1042626eb3c0c4819f7
URL:		http://pio.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	libgnome-devel >= 2.0.0
# rsvg program
BuildRequires:	librsvg
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper >= 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamesdir	%{_datadir}/games
%define		_gnomehelpsdir	%{_datadir}/gnome/help

%description
Pioneers, formerly known as Gnocatan, is an emulation of the board
game The Settlers of Catan, which can be played over the Internet.

%description -l pl.UTF-8
Gra Pioneers (znana wcześniej jako Gnocatan) jest emulacją gry
planszowej "Osadnicy z Catanu", w którą możemy grać przez Internet z
innymi graczami.

%package client
Summary:	Pioneers client
Summary(pl.UTF-8):	Klient gry Pioneers
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	yelp
Obsoletes:	gnocatan-client
Obsoletes:	gnocatan-data
Obsoletes:	gnocatan-help
Obsoletes:	pioneers-help

%description client
This is the game client which displays the board and interacts with a
player. It connects to a game server that can be local or on a remote
host.

%description client -l pl.UTF-8
Ten pakiet zawiera klienta gry, który wyświetla planszę i komunikuje
się z graczem. Łączy się z serwerem gry, który może być na maszynie
lokalnej lub zdalnej.

%package ai
Summary:	AI player for Pioneers game
Summary(pl.UTF-8):	Sztuczny gracz dla gry Pioneers
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ai
This package contains an AI player implementation that can take part
in Pioneers games.

%description ai -l pl.UTF-8
Ten pakiet zawiera implementację sztucznego gracza (AI), mogącego brać
udział w grach Pioneers.

%package editor
Summary:	Pioneers editor
Summary(pl.UTF-8):	Edytor dla gry Pioneers
Group:		X11/Applications/Games

%description editor
Pioneers editor.

%description editor -l pl.UTF-8
Edytor dla gry Pioneers.

%package server-data
Summary:	Pioneers data for server
Summary(pl.UTF-8):	Dane gry Pioneers dla serwera
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description server-data
The data package contains architecture independent data needed for the
game server.

%description server-data -l pl.UTF-8
Ten pakiet zawiera niezależne od architektury dane potrzebne dla
serwera gry.

%package server-console
Summary:	Console-based Pioneers game server
Summary(pl.UTF-8):	Konsolowy serwer gry Pioneers
Group:		Applications/Games
Requires:	%{name}-server-data = %{version}-%{release}
Obsoletes:	gnocatan-server

%description server-console
This package contains the Pioneers game server for the console which
accepts local or remote clients. One server instance must be running
per game. The game parameters are selected via command line options.

%description server-console -l pl.UTF-8
Ten pakiet zawiera serwer gry Pioneers dla konsoli, przyjmujący
lokalnych i zdalnych klientów. Dla każdej gry musi działać jedna
instancja serwera. Parametry gry ustawia się opcjami linii poleceń.

%package server-gtk
Summary:	GTK+-based Pioneers game server
Summary(pl.UTF-8):	Oparty na GTK+ serwer gry Pioneers
Group:		X11/Applications/Games
Requires:	%{name}-server-data = %{version}-%{release}
Obsoletes:	gnocatan-server

%description server-gtk
This package contains the GTK+-based Pioneers game server which
accepts local or remote clients. One server instance must be running
per game. Game parameters can be selected in a GUI dialog, and you can
also monitor connected players there.

%description server-gtk -l pl.UTF-8
Ten pakiet zawiera oparty na GTK+ serwer gry Pioneers, przyjmujący
lokalnych i zdalnych klientów. Dla każdej gry musi działać jedna
instancja serwera. Parametry gry mogą być wybierane w graficznym
okienku dialogowym; można w nim także monitorować podłączonych graczy.

%package meta-server
Summary:	Pioneers game meta server
Summary(pl.UTF-8):	Metaserwer gry Pioneers
Group:		Applications/Games

%description meta-server
This meta server for Pioneers accepts requests by clients to create
new game servers, and keeps a list of running servers one can connect
to.

%description meta-server -l pl.UTF-8
Ten pakiet zawiera metaserwer gry Pioneers, przyjmujący od klientów
żądania tworzenia nowych serwerów gry i utrzymujący listę działających
serwerów, z którymi klienci mogą się łączyć.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_gamesdir}/%{name}

%files client -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pioneers
%{_desktopdir}/pioneers.desktop
%dir %{_gamesdir}/%{name}/themes
%dir %{_gamesdir}/%{name}/themes/Classic
%dir %{_gamesdir}/%{name}/themes/FreeCIV-like
%dir %{_gamesdir}/%{name}/themes/Iceland
%dir %{_gamesdir}/%{name}/themes/Tiny
%dir %{_gamesdir}/%{name}/themes/Wesnoth-like
%{_gamesdir}/%{name}/themes/*/*.png
%{_gamesdir}/%{name}/themes/*/*.cfg
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_pixmapsdir}/pioneers.png
%{_mandir}/man6/pioneers.6*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/pioneers-C.omf

%files ai
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pioneersai
%{_mandir}/man6/pioneersai.6*
%{_gamesdir}/%{name}/computer_names

%files editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pioneers-editor
%{_desktopdir}/pioneers-editor.desktop
%{_pixmapsdir}/pioneers-editor.png
%{_mandir}/man6/pioneers-editor.6*

%files server-data
%defattr(644,root,root,755)
%{_gamesdir}/%{name}/*.game

%files server-console
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pioneers-server-console
%{_mandir}/man6/pioneers-server-console.6*

%files server-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pioneers-server-gtk
%{_desktopdir}/pioneers-server.desktop
%{_pixmapsdir}/pioneers-server.png
%{_mandir}/man6/pioneers-server-gtk.6*

%files meta-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pioneers-meta-server
%{_mandir}/man6/pioneers-meta-server.6*
