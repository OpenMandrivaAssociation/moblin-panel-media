Name: moblin-panel-media
Summary: Media panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.3
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-builroot

BuildRequires: libdbus-glib-devel
BuildRequires: clutter-devel
BuildRequires: nbtk-devel
BuildRequires: moblin-panel-devel
BuildRequires: bickley-devel
BuildRequires: bognor-regis-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: tdb-devel

%description
Moblin media panel

%prep
%setup -q 

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libexecdir}/*
%{_datadir}/*
