Name:       mapplauncherd-booster-nemomobile
Summary:    Application launch booster for nemomobile Components
Version:    0.0.0
Release:    1
Group:      System/Applications
License:    LGPLv2.1
URL:        https://github.com/nemomobile/mapplauncherd-booster-nemomobile
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  mapplauncherd-devel >= 4.1.0
BuildRequires:  pkgconfig(qdeclarative5-boostable)
Requires:  qt-components-qt5
Requires:  qt5-qtquickcontrols-nemo
Requires:  mapplauncherd >= 4.1.0

%description
Application launch booster for nemomobile Components applications

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

mkdir -p %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/
ln -s ../booster-nemomobile.service %{buildroot}/usr/lib/systemd/user/user-session.target.wants/

%files
%defattr(-,root,root,-)
%{_libexecdir}/mapplauncherd/booster-nemomobile
%{_datadir}/booster-nemomobile/*
%{_libdir}/systemd/user/booster-nemomobile.service
%{_libdir}/systemd/user/user-session.target.wants/booster-nemomobile.service

