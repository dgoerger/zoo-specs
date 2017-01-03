%define debug_package %{nil}
%global packname  BH
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.62.0.1
Release:          1%{?dist}
Summary:          Boost C++ Header Files

Group:            Applications/Engineering 
License:          BSL-1.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.62.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   
# Suggests:  
# LinkingTo:
# Enhances:





BuildRequires:    R-devel tex(latex) 



%description
Boost provides free peer-reviewed portable C++ source libraries.  A large
part of Boost is provided as C++ template code which is resolved entirely
at compile-time without linking.  This package aims to provide the most
useful subset of Boost libraries for template use among CRAN package. By
placing these libraries in this package, we offer a more efficient
distribution system for CRAN as replication of this code in the sources of
other packages is avoided. As of release 1.62.0-1, the following Boost
libraries are included: 'algorithm' 'any' 'atomic' 'bimap' 'bind'
'circular_buffer' 'concept' 'config' 'container' 'date'_'time' 'detail'
'dynamic_bitset' 'exception' 'filesystem' 'flyweight' 'foreach'
'functional' 'fusion' 'geometry' 'graph' 'heap' 'icl' 'integer'
'interprocess' 'intrusive' 'io' 'iostreams' 'iterator' 'math' 'move' 'mpl'
'multiprcecision' 'numeric' 'pending' 'phoenix' 'preprocessor'
'propery_tree' 'random' 'range' 'scope_exit' 'smart_ptr' 'spirit' 'tuple'
'type_traits' 'typeof' 'unordered' 'utility' 'uuid'.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include


%changelog
* Tue Dec 13 2016 deg38 <> 1.62.0.1-1
- initial package for Fedora
