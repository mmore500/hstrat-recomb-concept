#pragma once
#ifndef HSTRAT_RECOMB_CONCEPT_CONFIG_SETUP_CONFIG_NATIVE_HPP_INCLUDE
#define HSTRAT_RECOMB_CONCEPT_CONFIG_SETUP_CONFIG_NATIVE_HPP_INCLUDE

#include "Empirical/include/emp/config/ArgManager.hpp"

#include "try_read_config_file.hpp"

namespace hstrat_recomb_concept {

void setup_config_native(hstrat_recomb_concept::Config & config, int argc, char* argv[]) {
  auto specs = emp::ArgManager::make_builtin_specs(&config);
  emp::ArgManager am(argc, argv, specs);
  hstrat_recomb_concept::try_read_config_file(config, am);
}

} // namespace hstrat_recomb_concept

#endif // #ifndef HSTRAT_RECOMB_CONCEPT_CONFIG_SETUP_CONFIG_NATIVE_HPP_INCLUDE
