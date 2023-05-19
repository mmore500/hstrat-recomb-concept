#include <iostream>

#include "Empirical/include/emp/base/vector.hpp"

#include "hstrat_recomb_concept/config/Config.hpp"
#include "hstrat_recomb_concept/config/setup_config_native.hpp"
#include "hstrat_recomb_concept/example.hpp"

// This is the main function for the NATIVE version of Hereditary Stratigraph Recombination Proof of Concept.

hstrat_recomb_concept::Config cfg;

int main(int argc, char* argv[]) {
  // Set up a configuration panel for native application
  setup_config_native(cfg, argc, argv);
  cfg.Write(std::cout);

  std::cout << "Hello, world!" << "\n";

  return hstrat_recomb_concept::example();
}
