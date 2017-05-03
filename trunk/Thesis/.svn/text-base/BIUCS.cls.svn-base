 \NeedsTeXFormat{LaTeX2e}
 \ProvidesClass{BIUCS}[2011/02/14 BIU Theses and Dissertations]

% The BIUCS class is for producing theses and dissertations
% that meet the BIU requirements.
%
% The following class options are available
%
%   senior    : Produces the senior thesis preliminary pages (default)
%   masters   : Produces the masters thesis preliminary pages
%   phd       : Produces the PhD dissertation preliminary pages
%   honors    : Produces the honors thesis preliminary pages
%   noacknowledgments : Removes the acknowledgments page
%   etd : Removes blank pages necessary for double-sided printing without a fuss


% Declare some variables to hold the text fields for the preliminary pages

    \newcommand{\Title}[1]{\gdef\BIUField@Title{#1}}
    \newcommand{\Author}[1]{\gdef\BIUField@Author{#1}}
    \newcommand{\docname}[1]{\gdef\BIUField@DocName{#1}}
    \newcommand{\degree}[1]{\gdef\BIUField@Degree{#1}}
    \newcommand{\Advisor}[1]{\gdef\BIUField@Advisor{#1}}
    \newcommand{\AdvisorTitle}[1]{\gdef\BIUField@AdvisorTitle{#1}}
    \newcommand{\MemberA}[1]{\gdef\BIUField@MemberA{#1}}
    \newcommand{\MemberB}[1]{\gdef\BIUField@MemberB{#1}}
    \newcommand{\MemberC}[1]{\gdef\BIUField@MemberC{#1}}
    \newcommand{\MemberD}[1]{\gdef\BIUField@MemberD{#1}}
    \newcommand{\Month}[1]{\gdef\BIUField@Month{#1}}
    \newcommand{\Year}[1]{\gdef\BIUField@Year{#1}}
    \newcommand{\Abstract}[1]{\gdef\BIUField@Abstract{#1}}
    %\newcommand{\Keywords}[1]{\gdef\BIUField@Keywords{#1}}
    \newcommand{\Acknowledgments}[1]{\gdef\BIUField@Acknowledgments{#1}}
    \newcommand{\HonorsRepresentative}[1]{\gdef\BIUField@HonorsRep{#1}}

% Initialize the variables to their default values

    \Title{[Title: Titles Must Be in Mixed Case and May Not Exceed Six Inches on One Line\\
           and Must Be in the Inverted Pyramid Format When\\
           Additional Lines Are Needed]}
    \Author{[Student Name]}
    \docname{masters thesis}
    \degree{Master of Science}
    \Advisor{[Advisor]}
    \AdvisorTitle{Advisor}
    \MemberA{}
    \MemberB{}
    \MemberC{}
    \MemberD{}
    \Month{[Graduation Month]}
    \Year{[Year]}
    \Abstract{[The abstract is a summary of the thesis/dissertation with emphasis on the findings
              of the study. The abstract must not exceed 350 words in length and fit on one page,
              single spaced.]}
    %\Keywords{[A comma-separated list of descriptive words for search purposes]}
    \Acknowledgments{[Acknowledgements should be simple, in good taste, and fit on one page]}
    \HonorsRepresentative{[Honors Representative]}

% Define the preliminary page layouts using the variables

    \newcommand{\BIUtitlepage}{
        \thispagestyle{empty}
        {\centering
        \includegraphics[width=0.9\textwidth]{images/logo.jpg}\\[1cm]
		%\text{\Large M.Sc Thesis}\\[0.5cm]
		\vfill
		\hrule
		{ \vspace{2 mm} }
        \providecommand\pdfbookmark[3][]{} \pdfbookmark[0]{Title Page}{bm:Title}
        \parbox[t]{6in}{
            \renewcommand{\baselinestretch}{2} %\small\normalsize
            \huge \bfseries \centering\BIUField@Title\par
           % \renewcommand{\baselinestretch}{1} \small\normalsize
            }\\[\baselineskip]\par
        %\vfill
        %%{ \vspace{3 mm} }
        %{ \vspace{-20pt} }
        \hrule
        { \vspace{8 mm} } \vfill
        {\LARGE \BIUField@Author}\\[\baselineskip]
        \vfill
        {\large Submitted in partial fulfillment of the requirements for the
        Master's Degree in the Department of Computer Science, Bar-Ilan University}
        
        \vfill
        {\large Ramat Gan, Israel \hfill \BIUField@Year}
       
        
%         A \BIUField@DocName~submitted to the faculty of\\
%         Bar-Ilan University\\
%         in partial fulfillment of the requirements for the degree of\\[\baselineskip]
%         \BIUField@Degree \\
%         \vfill
%         Advisor: \BIUField@Advisor%, \BIUField@AdvisorTitle\\
%         \if \BIUField@MemberA \relax \relax \else \mbox{\BIUField@MemberA}\\ \fi
%         \if \BIUField@MemberB \relax \relax \else \mbox{\BIUField@MemberB}\\ \fi
%         \if \BIUField@MemberC \relax \relax \else \mbox{\BIUField@MemberC}\\ \fi
%         \if \BIUField@MemberD \relax \relax \else \mbox{\BIUField@MemberD}\\ \fi
%         \vfill
%         Department of Computer Science\\[\baselineskip]
%         Bar-Ilan University\\[\baselineskip]
%         \mbox{\BIUField@Month~\BIUField@Year} \\[\baselineskip]
%         
%         \vfill
%         Copyright \copyright\ \BIUField@Year~\BIUField@Author\\[\baselineskip]
%         All Rights Reserved\par
        }
        \newpage
        \thispagestyle{empty}
        { \large
        \noindent This work was carried out under the supervision of
        \BIUField@AdvisorTitle \BIUField@Advisor.
        \\
        Department of Computer Science, Bar-Ilan University. 
        }
        \clearemptydoublepage
      }


    \newcommand{\abstractpage}{
    	\newpage
        \thispagestyle{empty}
        {\centering
        \providecommand\pdfbookmark[3][]{} \pdfbookmark[0]{Abstract}{bm:Abstract}
        ABSTRACT\\[1\baselineskip]\par
        \renewcommand{\baselinestretch}{1} \small\normalsize
%         \parbox{\textwidth}{\centering\BIUField@Title}\\[1\baselineskip]\par
%         \mbox{\BIUField@Author}\\
%         Department of Computer Science\\
%         \mbox{\BIUField@Degree}\par
        }

        \addtolength{\parskip}{\baselineskip}
        %\singlespace
        \BIUField@Abstract\par

        \vfill
        \addtolength{\parskip}{-\baselineskip}
        %\noindent Keywords:~\BIUField@Keywords

        \clearemptydoublepage
    }

    \newcommand{\acknowledgmentspage}{
        \singlespace
        \thispagestyle{empty}
        {\centering
        \providecommand\pdfbookmark[3][]{} \pdfbookmark[0]{Acknowledgments}{bm:Acknowledge}
        ACKNOWLEDGMENTS\\[3\baselineskip]
        \par}\par
        \renewcommand{\baselinestretch}{1.66} \small\normalsize%
        \BIUField@Acknowledgments
        \par\renewcommand{\baselinestretch}{1} \small\normalsize%
        \clearemptydoublepage
        }

% Allow opt-out on acknowledgments
    \DeclareOption{noacknowlegments}{
      \renewcommand{\acknowledgmentspage}{}
    }



% Define the macro for making preliminary pages
    \newcommand{\makepreliminarypages}{
        \singlespace
        \changepage{0.5in}{}{}{}{}{}{-0.2in}{-0.3in}{}
        \BIUtitlepage
        \acknowledgmentspage
         % Make the table of contents.
         \changepage{-0.5in}{}{}{}{}{}{0.2in}{0.3in}{}
		\tableofcontents
		\listofalgorithms
		\changepage{0.5in}{}{}{}{}{}{-0.2in}{-0.3in}{}
        \abstractpage
        \renewcommand{\clearemptydoublepage}{\cle@remptydoublep@ge}
        \changepage{-0.5in}{}{}{}{}{}{0.2in}{0.3in}{}
        \doublespace
    }


    \DeclareOption{senior}{
      \degree{Bachelor of Science}
      \docname{thesis}
      \AdvisorTitle{Chair}
    }

    \DeclareOption{masters}{
      \degree{Master of Science}
      \docname{thesis}
      \AdvisorTitle{Advisor}
    }

    \DeclareOption{phd}{
      \degree{Doctor of Philosophy}
      \docname{dissertation}
      \AdvisorTitle{Chair}
    }
% Honors does their own thing...

    \DeclareOption{honors}{
      \renewcommand{\makepreliminarypages}{
        \changepage{0.5in}{-0.5in}{}{0.5in}{}{}{-0.2in}{-0.3in}{}
        \honorstitlepage
        \honorsabstractpage
        \acknowledgmentspage
        \renewcommand{\clearemptydoublepage}{\cle@remptydoublep@ge}
        \changepage{-0.5in}{}{}{}{}{}{0.2in}{0.3in}{}
        \doublespace
      }
    }

    \newcommand{\honorstitlepage}{
        \thispagestyle{empty}
        \begin{center}
        \providecommand\pdfbookmark[3][]{} \pdfbookmark[0]{Title Page}{bm:Title}
        \vspace*{0.375in}
        \parbox[t]{5in}{
            \renewcommand{\baselinestretch}{2} \small\normalsize
            \centering\BIUField@Title\par
            \renewcommand{\baselinestretch}{1} \small\normalsize
            }
        \vfill
        by\\[\baselineskip]
        \BIUField@Author
        \vfill
        Submitted to Bar-Ilan University in partial fulfillment\\[\baselineskip]
        of graduation requirements for University Honors
        \vfill
        Department of Computer Science\\[\baselineskip]
        Bar-Ilan University\\[\baselineskip]
        \BIUField@Month~\BIUField@Year
        \vfill
        \end{center}
        \parbox[b]{2.9in}{
            Advisor: \BIUField@Advisor \\[.5\baselineskip]
            }
        \hfill
        \parbox[b]{2.9in}{\singlespace
            Honors Representative: \BIUField@HonorsRep \\[.5\baselineskip]
            }
        \parbox[b]{2.9in}{
            Signature: \hrulefill}
        \hfill
        \parbox[b]{2.9in}{\singlespace
            Signature: \hrulefill}
        \clearemptydoublepage
      }

    \newcommand{\honorsabstractpage}{
        \thispagestyle{empty}
        {\centering
        \providecommand\pdfbookmark[3][]{} \pdfbookmark[0]{Abstract}{bm:Abstract}
        ABSTRACT\\[2\baselineskip]\par
        \renewcommand{\baselinestretch}{1} \small\normalsize
        \parbox{5in}{\centering\BIUField@Title}\\[1\baselineskip]\par
        \renewcommand{\baselinestretch}{2} \small\normalsize
        \mbox{\BIUField@Author}\\
        Department of Computer Science\\
        \mbox{\BIUField@Degree}\\[0.5\baselineskip]\par
        }

        \renewcommand{\baselinestretch}{1.66} \small\normalsize
        \BIUField@Abstract

        \clearemptydoublepage
    }

% A command to handle single sided preliminary pages in a double sided environment

    % Define the '\clearemptydoublepage' command to clear pages but not number any blank pages inserted.
    \let\cle@rdoublep@ge\cleardoublepage
    \newcommand{\cle@remptydoublep@ge}{
      \clearpage
      \if@twoside
      \ifodd\c@page\else
      \fi\fi
      {\pagestyle{empty}\cle@rdoublep@ge}}
    \newcommand{\clearemptydoublepage}{\cle@remptydoublep@ge}

\DeclareOption{etd}{
    \renewcommand{\clearemptydoublepage}{\clearpage}
    }


% Load the class and needed packages
    \DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
    \ProcessOptions
    \relax
    \LoadClass[letterpaper,12pt]{book}

    \RequirePackage{changepage}

% A couple of useful macros for line spacing

    % The \singlespace macro switches to single spaced lines
    \newcommand{\singlespace}{\par\renewcommand{\baselinestretch}{1}\small\normalsize\par}

    % The \doublespace macro switches to double spaced lines
    \newcommand{\doublespace}{\par\renewcommand{\baselinestretch}{1.66}\small\normalsize\par}


% Set the margins to BIU specifications

    \setlength{\marginparwidth}{0pt}
    \setlength{\marginparsep}{0pt}
    \setlength{\oddsidemargin}{0in}
    \setlength{\evensidemargin}{0in}
    \setlength{\textwidth}{6.5in}
    \setlength{\topmargin}{0in}
    \setlength{\headheight}{0.6cm}
    \setlength{\headsep}{0.3in}
    \setlength{\textheight}{8.4in}
    \setlength{\footskip}{0.25in}
    \raggedbottom

% Allow more liberal figure placement
    \renewcommand{\topfraction}{0.9}
    \renewcommand{\bottomfraction}{0.8}
    \setcounter{topnumber}{2}
    \setcounter{bottomnumber}{2}
    \setcounter{totalnumber}{4}
    \setcounter{secnumdepth}{3}
    \renewcommand{\textfraction}{0.07}

% Redefine the Table of Contents to deal with some blank page
% and bookmarking issues relating to ETD submission
    \let\TEMPtableofcontents\tableofcontents
    \renewcommand{\tableofcontents}{
      \clearemptydoublepage
      \singlespace
      \providecommand\phantomsection{} \phantomsection
      %\addcontentsline{toc}{chapter}{Table of Contents}
      \TEMPtableofcontents
      \clearemptydoublepage
      \doublespace
    }

% Redefine the List of Figures to deal with some blank page
% and bookmarking issues
    \let\TEMPlistoffigures\listoffigures
    \renewcommand{\listoffigures}{
      \providecommand\phantomsection{} \phantomsection
      \addcontentsline{toc}{chapter}{List of Figures}
      \TEMPlistoffigures
    }

% Redefine the Bibliography to deal with a bookmarking issues
    \let\TEMPbibliography\bibliography
    \renewcommand{\bibliography}{\clearemptydoublepage
      \singlespace
      \providecommand\phantomsection{} \phantomsection
      \addcontentsline{toc}{chapter}{Bibliography}
      \TEMPbibliography
    }

% The makeidx package makes your index for you.  To make an index entry,
% go to the place in the book that should be referenced and type
%  \index{key}
% An index entry labeled "key" (or whatever you type) will then
% be included and point to the correct page.
\usepackage{makeidx}
\makeindex

% Redefine the Index to deal with a bookmarking issues
    \let\TEMPprintindex\printindex
    \renewcommand{\printindex}{\clearemptydoublepage
      \providecommand\phantomsection{} \phantomsection
      \addcontentsline{toc}{chapter}{Index}
      \singlespace
      \TEMPprintindex
      \doublespace
    }

% These packages typeset the thesis with Times Roman font
\usepackage[T1]{fontenc}
%\usepackage{mathptmx}

% Allow the inclusion of graphics
\usepackage{graphicx}

% The fancyhdr package allows you to easily customize the page header.
% The settings below produce a nice, well separated header.
\usepackage{fancyhdr}
  \fancyhead{}
  \fancyhead[L]{\slshape \rightmark}
  \fancyhead[R,L]{\textbf{\thepage}}
  \fancyhead[R]{\slshape \leftmark}
%		For TwoSide Documents
%  \fancyhead[LO]{\slshape \rightmark}
%  \fancyhead[RO,LE]{\textbf{\thepage}}
%  \fancyhead[RE]{\slshape \leftmark}
  \fancyfoot{}
  \pagestyle{fancy}
  \renewcommand{\chaptermark}[1]{\markboth{\chaptername \ \thechapter \ \ #1}{}}
  \renewcommand{\sectionmark}[1]{\markright{\thesection \ \ #1}}

% The caption package allows you to change the formatting of figure captions.
% The commands here change to the suggested caption format:
% single spaced and a bold tag
\usepackage[margin=0.3in,labelfont=bf,labelsep=none]{caption}
 \DeclareCaptionFormat{suggested}{\singlespace#1#2 #3\par\doublespace}
 \captionsetup{format=suggested}

% Some useful packages
\usepackage{amsthm}%for theorems
\usepackage{amsmath}
\usepackage{url}
%\usepackage{subfigure}

    % This package makes straight single quotes in the Verbatim environment
    \usepackage{upquote}

    % This package lets us use custom Verbatim environments
    \usepackage{fancyvrb}
    \RecustomVerbatimEnvironment
      {Verbatim}{Verbatim}{xleftmargin=0.25in}

% Set the bibliography style
    \usepackage{cite}
    \bibliographystyle{abbrv}
    %\bibliographystyle{BIUCS}

% The hyperref package provides automatic linking and bookmarking for the table
% of contents, index, equation references, and figure references.  It must be
% included for the BIU Physics class to make a properly functioning electronic
% thesis.  It should be the last package loaded if possible.
%
% To include a link in your pdf use \href{URL}{Text to be displayed}.  If your
% display text is the URL, you probably should use the \url{} command discussed
% above.
%
% To add a bookmark in the pdf you can use \pdfbookmark.  You can look up its usage
% in the hyperref package documentation
%\usepackage[bookmarksnumbered,pdfpagelabels=true,plainpages=false,colorlinks=true,
%            linkcolor=black,citecolor=black,urlcolor=blue]{hyperref}
\urlstyle{rm}

\doublespace
