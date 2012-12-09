# revision 25809
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/appendixnumberbeamer
# catalog-date 2012-03-29 08:44:19 +0200
# catalog-license gpl3
# catalog-version undef
Name:		texlive-appendixnumberbeamer
Version:	20120329
Release:	1
Summary:	Manage frame numbering in appendixes in beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/appendixnumberbeamer
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package arranges that an appendix in a beamer presentation
is not counted in the frame count of the presentation;
appendixes are numbered starting from one.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/appendixnumberbeamer/appendixnumberbeamer.sty
%doc %{_texmfdistdir}/doc/latex/appendixnumberbeamer/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120329-1
+ Revision: 790522
- Import texlive-appendixnumberbeamer
- Import texlive-appendixnumberbeamer

