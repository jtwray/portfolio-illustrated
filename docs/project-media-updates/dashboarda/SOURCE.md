# Fixture provenance

Source: https://github.com/jtwray/dashboarda/blob/56a0b1b0aa7d2e571696e74f7f31a6568680aa67/apps/job-rates/index.html

Original source SHA-256: `cf0b74aa006632470540db96e9efdaf6346bfd355a005768f89b048a525e95a6`.

Copied from a read-only isolated clone of public Dashboarda main at that revision. The source repository was not modified.

Capture-only transformations:

- Replace task-ID footer with demonstration disclosure.
- Insert prominent demonstration-data banner.
- Remove localStorage read and replace the entire load/auth/fetch function with assignment of the embedded synthetic state and the original render call.
- Add three invented rows, three illustrative runs and a fixed illustrative sync timestamp. They demonstrate the renderer, not observed state, real hiring activity or continuous operation.
- Add Content-Security-Policy `default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src 'none'; connect-src 'none'`.
- For the separate PIN candidate, initialize the empty renderer and overlay a labeled DOM facsimile. No actual authentication functionality is present.

Layout, column mapping, render function, escaping and search behavior otherwise retain the original source. Fixtures are not verified screenshots. View them only in an authorized local environment. They are not referenced by portfolio site code.
