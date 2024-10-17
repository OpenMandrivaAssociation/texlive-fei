Name:		texlive-fei
Version:	65352
Release:	2
Summary:	Class for academic works at FEI University Center -- Brazil
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fei
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fei.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fei.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fei.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
fei is a class created by graduate students and LaTeX
enthusiasts that allows students from FEI University Center to
create their academic works, be it a monograph, masters
dissertation or phd thesis, under the typographic rules of the
institution. The class makes it possible to create a full
academic work, supporting functionalities such as cover, title
page, catalog entry, dedication, summary, lists of figures,
tables, algorithms, acronyms and symbols, multiple authors,
index, references, appendices and attachments. fei is loosely
based in the Brazilian National Standards Organization
(Associacao Brasileira de Normas Tecnicas, ABNT) standards for
the creation of academic works, such as ABNT NBR 10520:2002
(Citations) and ABNT NBR 6023:2002 (Bibliographic References).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fei
%{_texmfdistdir}/tex/latex/fei
%doc %{_texmfdistdir}/doc/latex/fei

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
