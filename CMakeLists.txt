cmake_minimum_required(VERSION 3.6.0)

project(mapplauncherd-booster-qtcomponents
	VERSION 0.2.0
	DESCRIPTION "mapplauncherd-booster-qtcomponents"
	LANGUAGES CXX)


set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

include(FeatureSummary)
include(GNUInstallDirs)

set(QT_MIN_VERSION "5.6.0")
find_package(Qt5 COMPONENTS Core Quick Concurrent REQUIRED)
find_package(PkgConfig REQUIRED)

pkg_check_modules(MAPPLAUNCHERDQT "qdeclarative5-boostable" REQUIRED)
pkg_check_modules(APPLAUNCHERD "applauncherd" REQUIRED)

SET(SRC
    src/eventhandler.cpp
    src/qmlbooster.cpp
)

SET(HEADERS
    src/eventhandler.h
    src/qmlbooster.h
)

add_executable(booster-nemomobile
    ${SRC}
    ${HEADERS}
)

include_directories(${APPLAUNCHERD_INCLUDE_DIRS} ${MAPPLAUNCHERDQT_INCLUDE_DIRS})

target_link_libraries(booster-nemomobile PUBLIC
    Qt5::Core
    Qt5::Quick
    Qt5::Concurrent
    ${MAPPLAUNCHERDQT_LIBRARIES}
    ${APPLAUNCHERD_LIBRARIES}
)

set_property(TARGET booster-nemomobile PROPERTY POSITION_INDEPENDENT_CODE TRUE)


install(TARGETS booster-nemomobile RUNTIME
    DESTINATION ${CMAKE_INSTALL_PREFIX}/libexec/mapplauncherd/)

install(FILES qml/preload.qml
    DESTINATION ${CMAKE_INSTALL_PREFIX}/share/booster-nemomobile)

install(FILES data/booster-nemomobile.service
    DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/systemd/user/)