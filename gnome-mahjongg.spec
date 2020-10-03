%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-mahjongg
Version:	3.38.1
Release:	1
Summary:	GNOME Mahjongg game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Mahjongg
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:  appstream-util
BuildRequires:  itstool
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:	libxml2-utils
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
%setup -q

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


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.1-3.mga5
+ Revision: 815339
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 739913
- Second Mageia 5 Mass Rebuild

* Mon Oct 13 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738334
- new version 3.14.1

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719239
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679732
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676933
- new version 3.13.92

* Tue Sep 02 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670829
- new version 3.13.91

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665295
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655348
- new version 3.13.4

* Mon Jun 23 2014 ovitters <ovitters> 3.13.1-3.mga5
+ Revision: 638832
- update url

* Sun Jun 15 2014 ovitters <ovitters> 3.13.1-2.mga5
+ Revision: 636447
- obsolete gnome-mahjongg-extra-data

* Thu May 29 2014 ovitters <ovitters> 3.13.1-1.mga5
+ Revision: 627594
- new version 3.13.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622277
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614225
- new version 3.12.1

* Sun Mar 23 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 606986
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604632
- new version 3.11.92

* Mon Mar 03 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599034
- new version 3.11.91

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593896
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 582994
- new version 3.11.5

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550451
- new version 3.10.2

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 542433
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 497548
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484360
- new version 3.10.0

* Tue Sep 17 2013 dams <dams> 3.9.92-1.mga4
+ Revision: 480589
- new version 3.9.92

* Tue Aug 27 2013 dams <dams> 3.9.90-1.mga4
+ Revision: 472181
- fix build by fixing bad dekstop file

  + fwang <fwang>
    - new version 3.9.90
    - cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.0-2.mga4
+ Revision: 440808
- Obsoletes 'gnome-games-extra-data'

* Sun Jun 09 2013 dams <dams> 3.8.0-1.mga4
+ Revision: 440764
- add 'libxml2-utils' as BR
- imported package gnome-mahjongg

