#pragma once
#ifndef HSTRAT_RECOMB_CONCEPT_CONFIG_TRY_READ_CONFIG_FILE_HPP_INCLUDE
#define HSTRAT_RECOMB_CONCEPT_CONFIG_TRY_READ_CONFIG_FILE_HPP_INCLUDE

#include <cstdlib>
#include <filesystem>
#include <iostream>

#include "Config.hpp"

namespace hstrat_recomb_concept {

void try_read_config_file(hstrat_recomb_concept::Config & config, emp::ArgManager & am) {
  if(std::filesystem::exists("hstrat_recomb_concept.cfg")) {
    std::cout << "Configuration read from hstrat_recomb_concept.cfg" << '\n';
    config.Read("hstrat_recomb_concept.cfg");
  }
  am.UseCallbacks();
  if (am.HasUnused())
    std::exit(EXIT_FAILURE);
}

} // namespace hstrat_recomb_concept

#endif // #ifndef HSTRAT_RECOMB_CONCEPT_CONFIG_TRY_READ_CONFIG_FILE_HPP_INCLUDE
