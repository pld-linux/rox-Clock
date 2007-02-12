%define _appsdir /usr/X11R6/share/ROX-apps
%define _name Clock
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Clock tells the time
Summary(pl.UTF-8):   ROX-Clock pokazuje czas
Name:		rox-%{_name}
Version:	1.3.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
Patch1:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#clock
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib-devel >= 0.2.2
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ROX-Clock is a panel or pinboard clock, with support for settings
alarms.

%description -l pl.UTF-8
ROX-Clock jest zegarem, który może być umieszczony na panelu lub
pulpicie. Umożliwia także ustawianie alarmów.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

rm -f ../install
install AppI* AppR* rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Clock $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

ln -sf AppRun $RPM_BUILD_ROOT%{_appsdir}/%{_name}/AppletRun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/rox_run
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/AppletRun
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
