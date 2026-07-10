%global tl_name appendixnumberbeamer
%global tl_revision 79061

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	Manage frame numbering in appendixes in beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/appendixnumberbeamer
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package fixes the frame numbering in beamer when using an appendix
such that the slides from the appendix are not counted in the total
frame number of the main part of the document. The total frame number
counter is reset to 0 when entering the appendix. The standard usage is
to include \usepackage{appendixnumberbeamer} in the preamble and then
declare the beginning of the appendix as usual using the \appendix
command.

