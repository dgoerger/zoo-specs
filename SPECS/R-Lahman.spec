%global packname  Lahman
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          5.0.0
Release:          1%{?dist}
Summary:          Sean 'Lahman' Baseball Database

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_5.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-dplyr
# Suggests:  R-lattice R-ggplot2 R-googleVis R-data.table R-vcd R-reshape2 R-tidyr R-zipcode
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-dplyr 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-dplyr 

%description
Provides the tables from the 'Sean Lahman Baseball Database' as a set of R
data.frames. It uses the data on pitching, hitting and fielding
performance and other tables from 1871 through 2015, as recorded in the
2016 version of the database.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Tue Dec 13 2016 deg38 <> 5.0.0-1
- initial package for Fedora
