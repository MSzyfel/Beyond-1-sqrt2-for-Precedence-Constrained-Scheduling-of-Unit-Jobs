# Manuscript requirements

This file records the author's requests for the standalone paper in this
directory. It is a reference for future revisions and audits.

## Scope and structure

- Base the article on `research/scheduling_metaoptimized_draft.tex` and retain
  the complete technical argument in a standalone manuscript.
- Provide a suitable title, an intuitive introduction, related work, a clear
  account of the paper's contribution, preliminaries, the technical sections,
  and conclusions.
- Present the problem and its motivation intuitively. Define the problem,
  notation, terminology, and nontrivial concepts without assuming familiarity
  with earlier papers.
- Cite prior results wherever used. Make clear which ideas and results are
  established and which are contributions of this manuscript. Follow the
  relevant earlier literature's terminology and conventions where appropriate.
- Audit and expand the related work to cover relevant variants and techniques.
  State the assumptions and scope of each cited result accurately.
- Aim for the standards of a leading research venue while maintaining an
  honest distinction between internal checking and independent validation.

## Proofs and exposition

- Give the entire proof and its calculations enough detail to be checked.
  Organize the reasoning into small, digestible lemmas and clear intermediate
  steps. Avoid long lemma statements and unnecessary remarks.
- Introduce objects before the lemmas that use them, rather than embedding
  their definitions in the lemma statements.
- State all relevant hypotheses and define nontrivial concepts, including
  notions such as Lipschitz continuity, when they are used.
- Prefer concise symbolic reasoning when it makes a derivation clearer.
  Maintain the explanations needed for the paper to be self-contained and
  easy to follow.
- Seek the simplest viable formal proof. Simplification must not sacrifice
  clarity, granularity, correctness, rigor, or overall quality.
- Keep the notation and arguments light while explaining each inference
  precisely. Simplicity is a priority, but never omit a step needed for a
  reader to verify or understand the proof.
- Use horizontal braces in calculations when they help readers identify the
  terms being grouped or bounded. Explain the marked relation where needed.
- Move optimization and parameter-verification details to an appendix. Present
  the resulting guarantee in the main text.
- Allow real or irrational optimization constants. Do not impose rational
  parameter choices or rational certification as goals. Prove any claimed
  guarantee, and retain the input and LP arithmetic assumptions needed for
  polynomial-time implementation.
- Do not mention code, verification programs, or implementation artifacts in
  the manuscript. Mathematical pseudocode is welcome where useful.

## Notation and mathematical style

- Keep notation brief, consistent, and aligned with the relevant literature.
  Where feasible, give each symbol a single meaning or a single type of object
  throughout the paper.
- Eliminate unnecessary aliases, especially renamings of symbols already in
  use. Prefer a longer formula to another symbol that readers must remember.
- Do not use an unqualified $e$ for a quantity that could be mistaken for
  Euler's number.
- Prefer `\mathcal` notation for complex objects where appropriate. Avoid
  word subscripts.
- State explicit domains for sums. Use square brackets for expectations.
  Use sums instead of integrals where that is simpler and mathematically valid.
- Use `\cdot` for multiplication throughout the manuscript, while retaining
  standard scheduling notation without `\cdot`.
- Introduce new terminology with `\emph`. Avoid semicolons and formulaic or
  artificial-sounding prose.

## Algorithms and figures

- Include pseudocode where it helps. Use `algorithm2e` and write the
  pseudocode symbolically with the manuscript's existing notation. Avoid
  introducing needless symbols or relying on descriptive instructions when a
  clear symbolic operation is available.
- Include figures when they clarify a substantive part of the argument.
  Examples should have enough size and structure to illustrate a nontrivial
  idea. Check that figures and captions accurately reflect the mathematics.
- Check the current Figure 2 independently against its definitions and proof.
  Compare it with the previous version and investigate any differences in
  correctness or the mathematical setting depicted.

## Continuing process

- Treat the manuscript as a long-term project. Work carefully through the
  entire writeup and continue improving it rather than making a superficial
  pass.
- For the current revision, pursue intensive work for the four-hour period
  requested by the author, using the time for successive substantive audits
  and improvements.
- Use several agents to explore simplifications, proof ideas, notation,
  exposition, references, figures, and other improvements in parallel.
- Repeatedly audit all requirements above and carry out independent checks of
  the proof, calculations, citations, notation, algorithms, figures, and
  assembled document. Investigate and resolve issues found in each pass.
- Keep mathematical validity and correct attribution ahead of brevity. Do
  not claim that internal checks establish external peer review or definitive
  literature priority.
