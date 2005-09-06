%define _name Clock
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Clock tells the time
Summary(pl):	ROX-Clock pokazuje czas
Name:		rox-%{_name}
Version:	2.1.4
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	1f19286b86c18a00694ed2caf81a460c
Source1:	%{name}.desktop
Patch0:		%{name}-ROX-CLib2-include.patch
Patch1:		%{name}-aclocal.patch
Patch2:		%{name}-ROX-apps-paths.patch
URL:		http://www.kerofin.demon.co.uk/rox/clock.html
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib2-devel >= 2.1.5-2
Requires:	rox >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-Clock is a panel or pinboard clock, with support for settings
alarms.

%description -l pl
ROX-Clock jest zegarem, który mo¿e byæ umieszczony na panelu lub
pulpicie. Umo¿liwia tak¿e ustawianie alarmów.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,Resources,%{_platform}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install AppR* *.xml rox_run $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install %{_platform}/Clock $RPM_BUILD_ROOT%{_roxdir}/%{_name}/%{_platform}
install Resources/alarm.png $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Resources
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox-Clock.png

sed -e "s,/lib/,/%{_lib}/," %{SOURCE1} > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

ln -sf AppRun $RPM_BUILD_ROOT%{_roxdir}/%{_name}/AppletRun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,README,Versions}
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%attr(755,root,root) %{_roxdir}/%{_name}/rox_run
%attr(755,root,root) %{_roxdir}/%{_name}/%{_platform}
%dir %{_roxdir}/%{_name}
%{_roxdir}/%{_name}/*xml
%{_roxdir}/%{_name}/AppletRun
%{_roxdir}/%{_name}/Help
%{_roxdir}/%{_name}/Resources
%{_desktopdir}/*
%{_pixmapsdir}/*
