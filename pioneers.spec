# TODO 
# - ?subpackage?, R, BR, ctrl+H in client
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
BuildRequires:	netpbm
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pioneers is an emulation of the board game The Settlers of Catan,
which can be played over the internet.

%description -l pl.UTF-8
Pioneers jest emulacją planszowej gry "Osadnicy z Catanu",
w którą możemy grać przez internet z innymi graczami.

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
%attr(755,root,root) %{_bindir}/pioneers
%attr(755,root,root) %{_bindir}/pioneers-editor
%attr(755,root,root) %{_bindir}/pioneers-meta-server
%attr(755,root,root) %{_bindir}/pioneers-server-console
%attr(755,root,root) %{_bindir}/pioneers-server-gtk
%attr(755,root,root) %{_bindir}/pioneersai
%{_desktopdir}/pioneers-editor.desktop
%{_desktopdir}/pioneers-server.desktop
%{_desktopdir}/pioneers.desktop
%dir %{_gamesdir}/%{name}
%{_gamesdir}/%{name}/*.game
%dir %{_gamesdir}/%{name}/themes
%dir %{_gamesdir}/%{name}/themes/FreeCIV-like
%dir %{_gamesdir}/%{name}/themes/Tiny
%dir %{_gamesdir}/%{name}/themes/Wesnoth-like
%dir %{_gamesdir}/%{name}/themes/Iceland
%{_gamesdir}/%{name}/themes/*/*.png
%{_gamesdir}/%{name}/themes/*/*.cfg
%{_gamesdir}/%{name}/themes/*.png
%{_mandir}/man6/pioneers-meta-server.6.gz
%{_mandir}/man6/pioneers-server-console.6.gz
%{_mandir}/man6/pioneers-server-gtk.6.gz
%{_mandir}/man6/pioneers.6.gz
%{_mandir}/man6/pioneersai.6.gz
%{_pixmapsdir}/pioneers-editor.png
%{_pixmapsdir}/pioneers-server.png
%{_pixmapsdir}/pioneers.png
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_gamesdir}/%{name}/computer_names
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/pioneers-C.omf
