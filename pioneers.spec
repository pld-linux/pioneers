# TODO 
# - description, R, BR, ctrl+H in client
# - add init file for server
%define		_gamesdir	%{_datadir}/games
Summary:	Pioneers - emulation of the board game "The Settlers of Catan".
Summary(pl.UTF-8):	Pioneers - emulacja planszowej gry "Osadnicy z Catanu".
Name:		pioneers
Version:	0.11.2
Release:	0.2
License:	GPL v2+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/pio/%{name}-%{version}.tar.gz
# Source0-md5:	4fb3ec61f5a084431fe46048bd30de9d
URL:		http://pio.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	librsvg-devel
BuildRequires:	libgcj-devel
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	pango-devel
BuildRequires:	netpbm
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pioneers,formerly known as Gnocatan, is an emulation of the board game The Settlers of Catan,
which can be played over the internet.

%description -l pl.UTF-8
Pioneers (znana też jako Gnocatan) jest emulacją planszowej gry "Osadnicy z Catanu",
w którą możemy grać przez internet z innymi graczami.

%package client
Summary:	-
Summary(pl.UTF-8):-
Group:	-

%description client
This is the game client which displays the board and interacts with
a player. It connects to a game server that can be local or on
a remote host.

%package editor
Summary:	-
Summary(pl.UTF-8):-
Group:	-

%description editor

%package server-gtk
Summary:	-
Summary(pl.UTF-8):-
Group:	-

%description server-gtk
This package contains the GTK-based Pioneers game server which accepts
local or remote clients. One server instance must be running per game.
Game parameters can be selected in a GUI dialog, and you can also
monitor connected players there.

%package server-data
Summary:	-
Summary(pl.UTF-8):-
Group:	-

%description server-data
The data package contains architecture independent data needed for
the game server.

%package server-console
Summary:	-
Summary(pl.UTF-8):  -
Group:	-

%description server-console
This package contains the Pioneers game server for the console which
accepts local or remote clients. One server instance must be running
per game. The game parameters are selected via command line options.

%package meta-server
Summary:	-
Summary(pl.UTF-8):	-
Group:-

%description meta-server
s meta server for Pioneers accepts requests by clients to create new
game servers, and keeps a list of running servers one can connect to.

%package ai
Summary:	-
Summary(pl.UTF-8):-
Group:	-

%description ai
This package contains an AI player implementation that can take part
in Pioneers games.

%package help
Summary:	-
Summary(pl.UTF-8):	-
Group:	-

%description help
This help package contains HTML documentation for the Pioneers client.

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_gamesdir}/%{name}

%files editor
%attr(755,root,root) %{_bindir}/pioneers-editor
%{_desktopdir}/pioneers-editor.desktop
%{_pixmapsdir}/pioneers-editor.png

%files server-gtk
%attr(755,root,root) %{_bindir}/pioneers-server-gtk
%{_desktopdir}/pioneers-server.desktop
%{_mandir}/man6/pioneers-server-gtk.6.gz
%{_pixmapsdir}/pioneers-server.png

%files server-data
%{_gamesdir}/%{name}/*.game

%files server-console
%attr(755,root,root) %{_bindir}/pioneers-server-console
%{_mandir}/man6/pioneers-server-console.6.gz

%files help 
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/pioneers-C.omf 

%files ai
%attr(755,root,root) %{_bindir}/pioneersai
%{_mandir}/man6/pioneersai.6.gz
%{_gamesdir}/%{name}/computer_names

%files meta-server
%attr(755,root,root) %{_bindir}/pioneers-meta-server
%{_mandir}/man6/pioneers-meta-server.6.gz

%files client
%attr(755,root,root) %{_bindir}/pioneers
%{_desktopdir}/pioneers.desktop
%dir %{_gamesdir}/%{name}/themes
%dir %{_gamesdir}/%{name}/themes/FreeCIV-like
%dir %{_gamesdir}/%{name}/themes/Tiny
%dir %{_gamesdir}/%{name}/themes/Wesnoth-like
%dir %{_gamesdir}/%{name}/themes/Iceland
%{_gamesdir}/%{name}/themes/*/*.png
%{_gamesdir}/%{name}/themes/*/*.cfg
%{_gamesdir}/%{name}/themes/*.png
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_pixmapsdir}/pioneers.png
%{_mandir}/man6/pioneers.6.gz
