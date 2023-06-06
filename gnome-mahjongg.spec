%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:		gnome-mahjongg
Version:	3.40.0
Release:	1
Summary:	GNOME Mahjongg game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Mahjongg
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  itstool
BuildRequires:  gtk-update-icon-cache
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  libxml2-utils
BuildRequires:  vala
# For fix build issue:  "error: Package `librsvg-2.0' not found in specified Vala API directories or GObject-Introspection GIR directories" (penguin)
BuildRequires:  librsvg-vala-devel
Obsoletes:	gnome-mahjongg-extra-data
# For help
Requires:	yelp

%description
Mahjongg is a simple pattern recognition game. You score points by
matching identical tiles.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_datadir}/applications/org.gnome.Mahjongg.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Mahjongg.gschema.xml
%{_mandir}/man6/%{name}.6*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/*/*/apps/org.gnome.Mahjongg*.*
%{_datadir}/metainfo/org.gnome.Mahjongg.appdata.xml
