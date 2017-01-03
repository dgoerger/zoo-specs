%global packname  latticeExtra
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.28
Release:          1%{?dist}
Summary:          Extra Graphical Utilities Based on Lattice

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-28.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-lattice R-RColorBrewer
# Imports:   R-grid R-stats R-utils R-grDevices
# Suggests:  R-maps R-mapproj R-deldir R-tripack R-zoo R-MASS R-quantreg R-mgcv
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-RColorBrewer 
Requires:         R-grid R-stats R-utils R-grDevices 
Requires:         R-maps R-mapproj R-deldir R-tripack R-zoo R-MASS R-quantreg R-mgcv 
BuildRequires:    R-devel tex(latex) R-lattice R-RColorBrewer
BuildRequires:    R-grid R-stats R-utils R-grDevices 
BuildRequires:   R-maps R-mapproj R-deldir R-tripack R-zoo R-MASS R-quantreg R-mgcv 

%description
Building on the infrastructure provided by the lattice package, this
package provides several new high-level functions and methods, as well as
additional utilities such as panel and axis annotation functions.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/old.svnlog
%{rlibdir}/%{packname}/scripts


%changelog
* Tue Dec 13 2016 deg38 <> 0.6.28-1
- initial package for Fedora
