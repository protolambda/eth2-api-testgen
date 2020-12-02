# Eth2 api testgen

This package generates tests for API client bindings.
I.e. it does not focus on pure spec correctness,
 but rather at enabling testing of the bindings with the latest server behavior.

This consists of two checks:
- that inputs become the correct URL and POST body
- that the response code and body can be parsed

However, API server implementations can still use this to compare their implementation against others.
Simply point this to your server implementation, and compare the generated results against an older version or completely different one.

## License

MIT, see [`LICENSE`](./LICENSE) file.


 