Name:           factory-rpm-macros
Version:        36
Release:        300%{?dist}
Summary:        Miscellaneous Factory RPM macros

License:        GPLv2+
Source0:        macros.factory

BuildArch:      noarch

%description
This package contains the miscellaneous Factory-related RPM macros.

%prep
echo <<END
%install_file 0 %{_rpmconfigdir}/macros.d/macros.factory
END

%install
# Can't use %%rpmmacrodir or %%install_src yet.
install -D -m 644 %{SOURCE0} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.factory


%files
%{_rpmconfigdir}/macros.d/macros.factory


%changelog
* Thu Oct 13 2022 Factory Linux Developers <info@factorylinux.com> 
- Built For The Factory Linux!
