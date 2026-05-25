# Skill: Godot Engine 4.6 — Referência Consolidada

> **Fonte**: Godot Engine Docs 4.6, godotengine.org
> **Alvo**: GDScript, game development, Godot 4.6
> **Última extração**: 2026-05-23 (sessão 35)

---

## Índice

| # | Seção |
|---|---|
| 1 | [Conceitos Fundamentais](#1-conceitos-fundamentais) |
| 1.1 | [Scene](#11-scene) |
| 1.2 | [Node](#12-node) |
| 1.3 | [Scene Tree](#13-scene-tree) |
| 1.4 | [Signal](#14-signal) |
| 2 | [Linguagens de Programação](#2-linguagens-de-programação) |
| 2.1 | [GDScript](#21-gdscript) |
| 2.2 | [C# e GDExtension](#22-c-e-gdextension) |
| 3 | [Design Philosophy](#3-design-philosophy) |
| 3.1 | [Composição e OOP](#31-composição-e-oop) |
| 3.2 | [Nodes não são Components](#32-nodes-não-são-components) |
| 3.3 | [O Editor é um Jogo Godot](#33-o-editor-é-um-jogo-godot) |
| 3.4 | [Motores 2D e 3D Separados](#34-motores-2d-e-3d-separados) |
| 4 | [Referência de Classe Integrada](#4-referência-de-classe-integrada) |
| 5 | [Workflow: Criando e Executando Scenes](#5-workflow-criando-e-executando-scenes) |
| 5.1 | [Criar uma Scene](#51-criar-uma-scene) |
| 5.2 | [Executar Scenes](#52-executar-scenes) |
| 6 | [Instancing de Scenes](#6-instancing-de-scenes) |
| 6.1 | [O que é Instancing](#61-o-que-é-instancing) |
| 6.2 | [Instancear no Editor](#62-instancear-no-editor) |
| 6.3 | [Editar Instances vs Scene-Template](#63-editar-instances-vs-scene-template) |
| 6.4 | [Scenes como Linguagem de Design](#64-scenes-como-linguagem-de-design) |
| 7 | [Primeiro Script GDScript](#7-primeiro-script-gdscript) |
| 7.1 | [Estrutura de um Script](#71-estrutura-de-um-script) |
| 7.2 | [Variáveis Membro e _process](#72-variáveis-membro-e-_process) |
| 7.3 | [Movimento com Vector2](#73-movimento-com-vector2) |
| 8 | [Input do Jogador](#8-input-do-jogador) |
| 8.1 | [Input Singleton vs Callbacks](#81-input-singleton-vs-callbacks) |
| 8.2 | [Ações de Input](#82-ações-de-input) |
| 9 | [Usando Signals](#9-usando-signals) |
| 9.1 | [Conectar Signal no Editor](#91-conectar-signal-no-editor) |
| 9.2 | [Conectar Signal via Código](#92-conectar-signal-via-código) |
| 9.3 | [Signals Customizados](#93-signals-customizados) |
| 10 | [Tutorial: Jogo 2D Completo (Dodge the Creeps)](#10-tutorial-jogo-2d-completo-dodge-the-creeps) |
| 10.1 | [Setup do Projeto](#101-setup-do-projeto) |
| 10.2 | [Scene do Player (Area2D)](#102-scene-do-player-area2d) |
| 10.3 | [Script do Player](#103-script-do-player) |
| 10.4 | [Scene do Mob (RigidBody2D)](#104-scene-do-mob-rigidbody2d) |
| 10.5 | [Main Scene e Spawning](#105-main-scene-e-spawning) |
| 10.6 | [HUD (CanvasLayer)](#106-hud-canvaslayer) |
| 11 | [Tutorial: Jogo 3D Completo (Squash the Creeps)](#11-tutorial-jogo-3d-completo-squash-the-creeps) |
| 11.1 | [Setup da Área de Jogo 3D](#111-setup-da-área-de-jogo-3d) |
| 11.2 | [Scene do Player 3D (CharacterBody3D)](#112-scene-do-player-3d-characterbody3d) |
| 11.3 | [Movimento 3D e Câmera](#113-movimento-3d-e-câmera) |
| 11.4 | [Scene do Mob 3D](#114-scene-do-mob-3d) |
| 11.5 | [Spawn Path e Spawning 3D](#115-spawn-path-e-spawning-3d) |
| 11.6 | [Physics Layers, Pulo e Squash](#116-physics-layers-pulo-e-squash) |
| 11.7 | [Morte do Player e Hitbox (Area3D)](#117-morte-do-player-e-hitbox-area3d) |
| 11.8 | [Score, Retry e Autoload](#118-score-retry-e-autoload) |
| 11.9 | [Animação 3D (AnimationPlayer)](#119-animação-3d-animationplayer) |
| 12 | [Boas Práticas](#12-boas-práticas) |
| 12.1 | [Organização de Scenes (Loose Coupling)](#121-organização-de-scenes-loose-coupling) |
| 12.2 | [Estrutura da Node Tree](#122-estrutura-da-node-tree) |
| 12.3 | [Scene vs Script](#123-scene-vs-script) |
| 12.4 | [Autoload — Quando Usar (e Quando Não Usar)](#124-autoload--quando-usar-e-quando-não-usar) |
| 12.5 | [Objetos Não-Node (Object, RefCounted, Resource)](#125-objetos-não-node-object-refcounted-resource) |
| 12.6 | [Interfaces e Aquisição de Referências](#126-interfaces-e-aquisição-de-referências) |
| 12.7 | [Notificações e Lifecycle](#127-notificações-e-lifecycle) |
| 12.8 | [Preferências de Dados](#128-preferências-de-dados) |
| 12.9 | [Preferências de Lógica](#129-preferências-de-lógica) |
| 12.10 | [Organização do Projeto](#1210-organização-do-projeto) |
| 12.11 | [VCS (Git)](#1211-vcs-git) |
| 13 | [GDScript Avançado](#13-gdscript-avançado) |
| 13.1 | [@export — Variantes e Agrupamentos](#131-export--variantes-e-agrupamentos) |
| 13.2 | [Tipagem Estática (Static Typing)](#132-tipagem-estática-static-typing) |
| 13.3 | [Format Strings](#133-format-strings) |
| 14 | [Física](#14-física) |
| 14.1 | [Tipos de Collision Objects](#141-tipos-de-collision-objects) |
| 14.2 | [Collision Layers e Masks](#142-collision-layers-e-masks) |
| 14.3 | [CharacterBody: Movimento e Colisão](#143-characterbody-movimento-e-colisão) |
| 15 | [Grupos, Resources e Save Game](#15-grupos-resources-e-save-game) |
| 15.1 | [Grupos](#151-grupos) |
| 15.2 | [Resources](#152-resources) |
| 15.3 | [Save Game (JSON + FileAccess)](#153-save-game-json--fileaccess) |
| 16 | [Animação Avançada](#16-animação-avançada) |
| 16.1 | [AnimationPlayer — Keyframes e Tracks](#161-animationplayer--keyframes-e-tracks) |
| 16.2 | [AnimationTree — Blending e StateMachine](#162-animationtree--blending-e-statemachine) |
| 17 | [Interface Gráfica (UI / Control)](#17-interface-gráfica-ui--control) |
| 17.1 | [Anchors e Tamanho de Controls](#171-anchors-e-tamanho-de-controls) |
| 17.2 | [Containers](#172-containers) |
| 17.3 | [Controls Customizados](#173-controls-customizados) |
| 17.4 | [Navegação por Teclado e Gamepad (Focus)](#174-navegação-por-teclado-e-gamepad-focus) |
| 18 | [Input Avançado](#18-input-avançado) |
| 18.1 | [InputEvent — Tipos e Fluxo de Propagação](#181-inputevent--tipos-e-fluxo-de-propagação) |
| 18.2 | [Teclado e Mouse](#182-teclado-e-mouse) |
| 18.3 | [Touch e Coordenadas do Mouse](#183-touch-e-coordenadas-do-mouse) |
| 18.4 | [Gamepads e Controles](#184-gamepads-e-controles) |
| 18.5 | [Encerramento da Aplicação (Quit)](#185-encerramento-da-aplicação-quit) |
| 19 | [Matemática (Math)](#19-matemática-math) |
| 19.1 | [Vetores — Operações Fundamentais](#191-vetores--operações-fundamentais) |
| 19.2 | [Planos e Detecção de Colisão (SAT)](#192-planos-e-detecção-de-colisão-sat) |
| 19.3 | [Transforms e Matrizes](#193-transforms-e-matrizes) |
| 19.4 | [Interpolação (Lerp)](#194-interpolação-lerp) |
| 19.5 | [Curvas Bezier e Caminhos](#195-curvas-bezier-e-caminhos) |
| 19.6 | [Números Aleatórios](#196-números-aleatórios) |
| 20 | [Performance](#20-performance) |
| 20.1 | [Princípios de Otimização](#201-princípios-de-otimização) |
| 20.2 | [Otimização de CPU](#202-otimização-de-cpu) |
| 20.3 | [Otimização de GPU](#203-otimização-de-gpu) |
| 20.4 | [Optimization using Servers (Low-level API)](#204-optimization-using-servers-low-level-api) |
| 20.5 | [Threads](#205-threads) |
| 20.6 | [Occlusion Culling](#206-occlusion-culling) |
| 20.7 | [LOD (Level of Detail)](#207-lod-level-of-detail) |
| 21 | [Networking](#21-networking) |
| 21.1 | [High-level Multiplayer (ENet / RPC)](#211-high-level-multiplayer-enet--rpc) |
| 21.2 | [HTTP Requests](#212-http-requests) |
| 22 | [Export](#22-export) |
| 22.1 | [Workflow de Export](#221-workflow-de-export) |
| 22.2 | [Arquivos de Configuração](#222-arquivos-de-configuração) |
| 22.3 | [Export pela Linha de Comando](#223-export-pela-linha-de-comando) |
| 22.4 | [PCK vs ZIP](#224-pck-vs-zip) |
| 22.5 | [DLC, Patches e Mods (Resource Packs em Runtime)](#225-dlc-patches-e-mods-resource-packs-em-runtime) |
| 23 | [Navigation](#23-navigation) |
| 23.1 | [Visão Geral — Objetos de Navegação](#231-visão-geral--objetos-de-navegação) |
| 23.2 | [Setup Mínimo (2D)](#232-setup-mínimo-2d) |
| 23.3 | [NavigationServer — Sincronização e Threading](#233-navigationserver--sincronização-e-threading) |
| 23.4 | [NavigationPaths](#234-navigationpaths) |
| 23.5 | [NavigationAgent — Pathfinding, Following e Avoidance](#235-navigationagent--pathfinding-following-e-avoidance) |
| 23.6 | [NavigationObstacles](#236-navigationobstacles) |
| 23.7 | [NavigationLayers](#237-navigationlayers) |
| 23.8 | [Debug de Navegação](#238-debug-de-navegação) |
| 23.9 | [Otimização de Performance de Navegação](#239-otimização-de-performance-de-navegação) |
| 24 | [TileMaps](#24-tilemaps) |
| 24.1 | [TileSet — Atlas e Configuração](#241-tileset--atlas-e-configuração) |
| 24.2 | [Collision, Navigation e Occlusion no TileSet](#242-collision-navigation-e-occlusion-no-tileset) |
| 24.3 | [Terrain Sets (Autotiling)](#243-terrain-sets-autotiling) |
| 24.4 | [TileMapLayer — Configuração e Layers](#244-tilemaplayer--configuração-e-layers) |
| 24.5 | [Editor de TileMap — Modos de Pintura](#245-editor-de-tilemap--modos-de-pintura) |
| 24.6 | [Alternative Tiles, Patterns e Randomização](#246-alternative-tiles-patterns-e-randomização) |
| 25 | [Export por Plataforma](#25-export-por-plataforma) |
| 25.1 | [Windows](#251-windows) |
| 25.2 | [Linux](#252-linux) |
| 25.3 | [macOS](#253-macos) |
| 25.4 | [Android](#254-android) |
| 25.5 | [iOS](#255-ios) |
| 25.6 | [Web (HTML5)](#256-web-html5) |
| 25.7 | [Servidor Dedicado (Headless)](#257-servidor-dedicado-headless) |
| 26 | [File e Data I/O](#26-file-e-data-io) |
| 26.1 | [Caminhos de Arquivo (res:// e user://)](#261-caminhos-de-arquivo-res-e-user) |
| 26.2 | [FileAccess — Leitura e Escrita](#262-fileaccess--leitura-e-escrita) |
| 26.3 | [Save Game — Referência Rápida](#263-save-game--referência-rápida) |
| 26.4 | [Carregamento em Background (ResourceLoader Threaded)](#264-carregamento-em-background-resourceloader-threaded) |
| 26.5 | [Carregamento de Arquivos em Runtime](#265-carregamento-de-arquivos-em-runtime) |
| 27 | [Áudio](#27-áudio) |
| 27.1 | [Audio Buses](#271-audio-buses) |
| 27.2 | [AudioStreamPlayer — Tipos e Uso](#272-audiostreamplayer--tipos-e-uso) |
| 27.3 | [Sincronização de Áudio com Gameplay](#273-sincronização-de-áudio-com-gameplay) |
| 28 | [Shaders](#28-shaders) |
| 28.1 | [Introdução — O que são Shaders](#281-introdução--o-que-são-shaders) |
| 28.2 | [Tipos de Shader e Render Modes](#282-tipos-de-shader-e-render-modes) |
| 28.3 | [Shading Language — Tipos e Uniforms](#283-shading-language--tipos-e-uniforms) |
| 28.4 | [Primeiro Shader 2D](#284-primeiro-shader-2d) |
| 28.5 | [ShaderMaterial vs StandardMaterial3D](#285-shadermaterial-vs-standardmaterial3d) |
| 29 | [Internacionalização (i18n)](#29-internacionalização-i18n) |
| 29.1 | [Setup: Importar e Registrar Traduções](#291-setup-importar-e-registrar-traduções) |
| 29.2 | [Detecção Automática e TranslationServer](#292-detecção-automática-e-translationserver) |
| 29.3 | [Tradução de Strings: tr(), tr_n(), Contextos e Pluralização](#293-tradução-de-strings-tr-tr_n-contextos-e-pluralização) |
| 29.4 | [CSV (Planilhas)](#294-csv-planilhas) |
| 29.5 | [gettext (PO/POT)](#295-gettext-popot) |
| 29.6 | [Recursos Localizados (Remaps)](#296-recursos-localizados-remaps) |
| 29.7 | [Bidirectional (BiDi) e RTL](#297-bidirectional-bidi-e-rtl) |
| 29.8 | [Pseudolocalização](#298-pseudolocalização) |
| 30 | [Renderers — Visão Geral](#30-renderers--visão-geral) |
| 30.1 | [Os Três Renderers](#301-os-três-renderers) |
| 30.2 | [Comparação de Features](#302-comparação-de-features) |
| 31 | [Iluminação 3D Avançada](#31-iluminação-3d-avançada) |
| 31.1 | [Tipos de Luz 3D](#311-tipos-de-luz-3d) |
| 31.2 | [Shadow Mapping 3D](#312-shadow-mapping-3d) |
| 31.3 | [Shadow Atlas (OmniLight / SpotLight)](#313-shadow-atlas-omnilight--spotlight) |
| 32 | [Environment e Post-Processing](#32-environment-e-post-processing) |
| 32.1 | [WorldEnvironment e CameraAttributes](#321-worldenvironment-e-cameraattributes) |
| 32.2 | [Background, Sky Materials e Ambient Light](#322-background-sky-materials-e-ambient-light) |
| 32.3 | [Tonemapping](#323-tonemapping) |
| 32.4 | [Screen-Space Effects (SSR, SSAO, SSIL)](#324-screen-space-effects-ssr-ssao-ssil) |
| 32.5 | [Glow e Fog](#325-glow-e-fog) |
| 32.6 | [TAA e FSR 2.2](#326-taa-e-fsr-22) |
| 33 | [Luzes e Sombras 2D](#33-luzes-e-sombras-2d) |
| 33.1 | [Nodes de Iluminação 2D](#331-nodes-de-iluminação-2d) |
| 33.2 | [PointLight2D e DirectionalLight2D](#332-pointlight2d-e-directionallight2d) |
| 33.3 | [LightOccluder2D e Sombras](#333-lightoccluder2d-e-sombras) |
| 33.4 | [Normal e Specular Maps em 2D](#334-normal-e-specular-maps-em-2d) |
| 34 | [GDExtension](#34-gdextension) |
| 34.1 | [O que é GDExtension](#341-o-que-é-gdextension) |
| 34.2 | [Arquivo .gdextension — Estrutura](#342-arquivo-gdextension--estrutura) |
| 35 | [Editor Plugins](#35-editor-plugins) |
| 35.1 | [Plugin Básico — Estrutura e Ciclo de Vida](#351-plugin-básico--estrutura-e-ciclo-de-vida) |
| 35.2 | [Custom Node (nó customizado)](#352-custom-node-nó-customizado) |
| 35.3 | [Custom Dock (painel customizado)](#353-custom-dock-painel-customizado) |
| 35.4 | [Main Screen Plugin (aba central)](#354-main-screen-plugin-aba-central) |
| 35.5 | [Registrando Autoloads em Plugins](#355-registrando-autoloads-em-plugins) |
| 35.6 | [Sub-plugins](#356-sub-plugins) |
| 35.7 | [Import Plugin (EditorImportPlugin)](#357-import-plugin-editorimportplugin) |
| 35.8 | [Inspector Plugin (EditorInspectorPlugin + EditorProperty)](#358-inspector-plugin-editorinspectorplugin--editorproperty) |
| 35.9 | [Visual Shader Plugin (VisualShaderNodeCustom)](#359-visual-shader-plugin-visualshadernodecustom) |
| 35.10 | [3D Gizmo Plugin (EditorNode3DGizmoPlugin)](#3510-3d-gizmo-plugin-editornode3dgizmoplugin) |
| 36 | [Múltiplas Resoluções](#36-múltiplas-resoluções) |
| 36.1 | [Conceito — Base Size e Viewport](#361-conceito--base-size-e-viewport) |
| 36.2 | [Stretch Mode](#362-stretch-mode) |
| 36.3 | [Stretch Aspect](#363-stretch-aspect) |
| 36.4 | [Stretch Scale e Scale Mode](#364-stretch-scale-e-scale-mode) |
| 36.5 | [Recomendações por Cenário](#365-recomendações-por-cenário) |
| 36.6 | [hiDPI](#366-hidpi) |
| 36.7 | [Campo de Visão 3D em Múltiplos Aspectos](#367-campo-de-visão-3d-em-múltiplos-aspectos) |
| 37 | [@tool — Executando Código no Editor](#37-tool--executando-código-no-editor) |
| 37.1 | [O que é `@tool`](#371-o-que-é-tool) |
| 37.2 | [Uso Básico](#372-uso-básico) |
| 37.3 | [Propriedades Exportadas com Setter](#373-propriedades-exportadas-com-setter) |
| 37.4 | [Aviso de Configuração do Node](#374-aviso-de-configuração-do-node) |
| 37.5 | [Monitorar Mudanças em Resources](#375-monitorar-mudanças-em-resources) |
| 37.6 | [EditorScript — Scripts One-off](#376-editorscript--scripts-one-off) |
| 37.7 | [Instancing de Scenes no Editor](#377-instancing-de-scenes-no-editor) |
| 37.8 | [Debug](#378-debug) |
| 38 | [Viewports](#38-viewports) |
| 38.1 | [Visão Geral](#381-visão-geral) |
| 38.2 | [SubViewport como Render Target](#382-subviewport-como-render-target) |
| 38.3 | [Input e Listener](#383-input-e-listener) |
| 38.4 | [Câmeras](#384-câmeras) |
| 38.5 | [Worlds (2D e 3D)](#385-worlds-2d-e-3d) |
| 38.6 | [Captura de Tela (Screenshot)](#386-captura-de-tela-screenshot) |
| 38.7 | [SubViewportContainer](#387-subviewportcontainer) |
| 38.8 | [Opções de Renderização](#388-opções-de-renderização) |
| 39 | [Compositor e Custom Post-Processing](#39-compositor-e-custom-post-processing) |
| 39.1 | [Compositor — Visão Geral](#391-compositor--visão-geral) |
| 39.2 | [CompositorEffect — Implementação](#392-compositoreffect--implementação) |
| 39.3 | [Custom Post-Processing (Canvas Layer)](#393-custom-post-processing-canvas-layer) |
| 40 | [XR / Realidade Virtual e Aumentada](#40-xr--realidade-virtual-e-aumentada) |
| 40.1 | [Visão Geral — Sistema XR](#401-visão-geral--sistema-xr) |
| 40.2 | [Setup da Cena XR](#402-setup-da-cena-xr) |
| 40.3 | [Script de Inicialização XR (Completo)](#403-script-de-inicialização-xr-completo) |
| 40.4 | [OpenXR — Configurações](#404-openxr--configurações) |
| 40.5 | [Action Map XR](#405-action-map-xr) |
| 40.6 | [AR / Passthrough](#406-ar--passthrough) |
| 40.7 | [Room Scale — Movimento com Física](#407-room-scale--movimento-com-física) |
| 40.8 | [Composition Layers (UI 2D em XR)](#408-composition-layers-ui-2d-em-xr) |
| 40.9 | [Hand Tracking](#409-hand-tracking) |
| 40.10 | [Body Tracking e Render Models](#4010-body-tracking-e-render-models) |
| 40.11 | [XR Fullscreen Effects](#4011-xr-fullscreen-effects) |
| 40.12 | [Deploy Android e XR Tools](#4012-deploy-android-e-xr-tools) |
| 41 | [Engine Architecture](#41-engine-architecture) |
| 41.1 | [Visão Geral da Arquitetura](#411-visão-geral-da-arquitetura) |
| 41.2 | [Métodos e Macros Comuns (C++)](#412-métodos-e-macros-comuns-c) |
| 41.3 | [Core Types](#413-core-types) |
| 41.4 | [Variant](#414-variant) |
| 41.5 | [Object class](#415-object-class) |
| 41.6 | [Inheritance Class Tree](#416-inheritance-class-tree) |
| 42 | [Unit Testing C++](#42-unit-testing-c) |
| 42.1 | [Plataformas, Build e Execução](#421-plataformas-build-e-execução) |
| 42.2 | [Escrevendo Testes (TEST_CASE / SUBCASE)](#422-escrevendo-testes-test_case--subcase) |
| 42.3 | [Assertions e Logging](#423-assertions-e-logging) |
| 42.4 | [Tags Especiais e Testing de Signals](#424-tags-especiais-e-testing-de-signals) |
| 42.5 | [Test Tools (REGISTER_TEST_COMMAND)](#425-test-tools-register_test_command) |
| 42.6 | [Integration Tests para GDScript](#426-integration-tests-para-gdscript) |
| 43 | [Custom Modules C++](#43-custom-modules-c) |
| 43.1 | [Quando usar Módulos vs GDExtension](#431-quando-usar-módulos-vs-gdextension) |
| 43.2 | [Estrutura de um Módulo (Arquivos Obrigatórios)](#432-estrutura-de-um-módulo-arquivos-obrigatórios) |
| 43.3 | [Compilando e Usando o Módulo](#433-compilando-e-usando-o-módulo) |
| 43.4 | [Compilação Externa (custom_modules)](#434-compilação-externa-custom_modules) |
| 43.5 | [Ordem de Inicialização (preregister)](#435-ordem-de-inicialização-preregister) |
| 43.6 | [Documentação e Ícones Customizados](#436-documentação-e-ícones-customizados) |
| 43.7 | [Unit Tests em Módulos](#437-unit-tests-em-módulos) |
| 43.8 | [Regras e Sumário](#438-regras-e-sumário) |
| 44 | [Custom Godot Servers (C++)](#44-custom-godot-servers-c) |
| 44.1 | [Estrutura de um Server](#441-estrutura-de-um-server) |
| 44.2 | [RID-Based Resource Data](#442-rid-based-resource-data) |
| 44.3 | [Dummy Class e GDScript Binding](#443-dummy-class-e-gdscript-binding) |
| 44.4 | [MessageQueue](#444-messagequeue) |
| 45 | [Custom Resource Format Loaders](#45-custom-resource-format-loaders) |
| 45.1 | [ResourceFormatLoader](#451-resourceformatloader) |
| 45.2 | [ResourceFormatSaver](#452-resourceformatsaver) |
| 45.3 | [Custom Data Type e Registro](#453-custom-data-type-e-registro) |
| 46 | [Custom AudioStreams (C++)](#46-custom-audiostreams-c) |
| 46.1 | [AudioStream + AudioStreamPlayback](#461-audiostream--audiostreamplayback) |
| 46.2 | [Resampling (AudioStreamPlaybackResampled)](#462-resampling-audiostreamplaybackresampled) |
| 47 | [Custom Platform Ports (C++)](#47-custom-platform-ports-c) |
| 47.1 | [Visão Geral e Requisitos de RAM](#471-visão-geral-e-requisitos-de-ram) |
| 47.2 | [Arquivos Obrigatórios (OS singleton + detect.py + logo.svg)](#472-arquivos-obrigatórios-os-singleton--detectpy--logosvg) |
| 47.3 | [Features Opcionais](#473-features-opcionais) |
| 47.4 | [Distribuição](#474-distribuição) |
| 48 | [Build do Engine (Compilação a partir do Código-Fonte)](#48-build-do-engine-compilação-a-partir-do-código-fonte) |
| 48.1 | [Sistema de Build (SCons)](#481-sistema-de-build-scons) |
| 48.2 | [Targets e Plataformas](#482-targets-e-plataformas) |
| 48.3 | [Opções de Otimização de Tamanho](#483-opções-de-otimização-de-tamanho) |
| 48.4 | [Compatibilidade de API (compat.inc)](#484-compatibilidade-de-api-compatinc) |
| 49 | [Debugging e Profiling do Engine](#49-debugging-e-profiling-do-engine) |
| 49.1 | [Sanitizers](#491-sanitizers) |
| 49.2 | [C++ Profilers](#492-c-profilers) |
| 50 | [Desenvolvimento do Editor e Formatos de Arquivo](#50-desenvolvimento-do-editor-e-formatos-de-arquivo) |
| 50.1 | [Estrutura do Código do Editor](#501-estrutura-do-código-do-editor) |
| 50.2 | [Ícones do Editor (SVG)](#502-ícones-do-editor-svg) |
| 50.3 | [Formato TSCN (Cenas e Resources em Texto)](#503-formato-tscn-cenas-e-resources-em-texto) |
| 51 | [Asset Library](#51-asset-library) |
| 51.1 | [Tipos de Assets](#511-tipos-de-assets) |
| 51.2 | [Usando a Asset Library no Editor](#512-usando-a-asset-library-no-editor) |
| 51.3 | [Requisitos de Submissão](#513-requisitos-de-submissão) |
| 51.4 | [Recomendações de Submissão](#514-recomendações-de-submissão) |
| 51.5 | [Formulário de Submissão — Campos](#515-formulário-de-submissão--campos) |

---

## 1. Conceitos Fundamentais

Todo jogo em Godot é uma **árvore de nodes agrupados em scenes**, com nodes se comunicando via **signals**.

### 1.1 Scene

- Uma Scene é a unidade reutilizável fundamental em Godot — pode representar um personagem, uma arma, um menu, um nível, ou qualquer elemento do jogo.
- **Regra**: Scenes preenchem o papel de *prefabs* e de *cenas* de outros engines simultaneamente — use-as para ambos os propósitos.
- Scenes podem ser **aninhadas**: uma scene pode conter outra como filho.
- Scenes podem ser **herdadas**: crie uma scene `Magician` que estende `Character`; alterações em `Character` propagam para `Magician`.
- Ao salvar uma árvore de nodes como scene, ela aparece no editor como um único node (estrutura interna oculta).
- Toda scene tem exatamente **um root node** — o node raiz identifica a scene (ex.: "Player" em uma scene de personagem).
- Scenes são salvas em disco como `.tscn`; múltiplas instâncias da mesma scene podem coexistir simultaneamente no jogo.

### 1.2 Node

- Node é o **menor bloco de construção** do jogo. Scenes são compostas de um ou mais nodes.
- Nodes são organizados em **árvores** e sempre herdam de seus pais até a classe `Node`.
- A maioria dos nodes funciona **independentemente** uns dos outros.
- Todo node possui: nome único, propriedades editáveis no Inspector, callback a cada frame, extensibilidade via script, e pode ser adicionado como filho de outro node.
- Sufixo `2D` indica node de cena 2D; sufixo `3D` indica 3D. Nodes que antes se chamavam "Spatial" são agora `Node3D` a partir do Godot 4.

> 💡 Nota: `Sprite2D` é simultaneamente `Node2D`, `CanvasItem` e `Node` — herda propriedades e features de todas as classes pai (transforms, desenho customizado, shaders).

- **Scripts** se anexam a um node e estendem seu comportamento — herdam automaticamente todas as funções e propriedades do node ao qual estão associados.

### 1.3 Scene Tree

- A **Scene Tree** é a árvore global de todas as scenes do jogo em execução — literalmente uma árvore de scenes, que por sua vez são árvores de nodes.
- Pense o jogo em termos de scenes (personagens, armas, portas, UI), não de nodes individuais.

### 1.4 Signal

- Nodes emitem **signals** quando eventos ocorrem. Signals permitem comunicação entre nodes sem acoplamento direto de código.
- **Regra**: Use signals para comunicação entre nodes em vez de referências diretas, preservando a flexibilidade da estrutura de scenes.
- Signals são a implementação Godot do padrão **Observer**.
- É possível definir signals customizados para o jogo.

> 💡 Nota: Exemplos de signals embutidos: botão pressionado, colisão entre objetos, personagem entrando em uma área.

---

## 2. Linguagens de Programação

### 2.1 GDScript

- GDScript é a linguagem **primária e recomendada** do Godot para iniciantes e para a maioria dos projetos.
- **Regra**: Prefira GDScript a C# para projetos novos — foi projetado especificamente para as necessidades de game developers e game designers, com integração profunda ao engine e ao editor.
- Sintaxe baseada em **indentação**; detecta tipos e oferece auto-complete de qualidade equivalente a linguagens estáticas.
- Possui **tipos embutidos** otimizados para gameplay: `Vector2`, `Vector3`, `Color`, etc.
- Godot é baseado em **OOP** — seja confortável com classes e objetos.

> 💡 Nota: GDScript é específico do Godot, mas as técnicas aprendidas nele se aplicam a outras linguagens de programação.

Características adicionais do GDScript:
- **Sem garbage collector** — o engine usa contagem de referências e gerencia memória automaticamente na maioria dos casos; controle manual de memória disponível quando necessário.
- **Gradual typing** — variáveis têm tipos dinâmicos por padrão; type hints opcionais ativam checagem estrita de tipos.
- **Threads** — suporte a múltiplas threads tão eficiente quanto linguagens de tipo estático.
- **Compilação rápida** — tempos de compilação e carregamento baixos.
- **Tipos vetoriais embutidos** — `Vector2`, `Vector3`, `Transform2D`, `Transform3D` etc., otimizados para álgebra linear intensiva.

### 2.2 C# e GDExtension

- **C#** é suportado e popular na indústria de jogos — segunda opção oficial.
- **GDExtension** permite escrever código de alta performance em C, C++, Rust, D, Haxe ou Swift **sem recompilar o engine**.
- Use GDExtension para integrar bibliotecas de terceiros e SDKs ao engine.
- **GDExtension** é a melhor opção para performance máxima — não precisa ser usado em todo o jogo; pode ser combinado com GDScript ou C# nas demais partes.
- **Regra**: É possível usar múltiplas linguagens no mesmo projeto — por exemplo, lógica de gameplay em GDScript (rápido de escrever) e algoritmos pesados em C++ (performance máxima).
- C# requer a **edição .NET do editor Godot** (download separado em godotengine.org/download); necessita de editor externo como VSCode ou Visual Studio.

> ⚠ Evite: Exportar projetos C# para a **plataforma web** no Godot 4 — não é suportado. Para C# na web, use Godot 3. Suporte a Android/iOS existe desde Godot 4.2, mas é experimental.

---

## 3. Design Philosophy

### 3.1 Composição e OOP

- **Regra**: Estruture o projeto como composição/agregação de scenes — não como hierarquia rígida de classes.
- Godot favorece **composição** (scenes aninhadas) e **herança de scenes** em vez de padrões de programação estritos.
- Uma scene funciona como uma classe em código puro, mas pode ser construída no editor, só em código, ou misturando os dois.

**Exemplo de composição:**
```
BlinkingLight (scene)
  └── BrokenLantern (scene usa BlinkingLight)
        └── City (nível com muitos BrokenLanterns)
```
Alterar `BlinkingLight` propaga instantaneamente para todos os `BrokenLantern` na cena.

**Exemplo de herança:**
```
Character (scene base)
  └── Magician (scene herdada de Character)
```
Modificar `Character` no editor atualiza `Magician` automaticamente.

### 3.2 Nodes não são Components

> ⚠ Evite: Pensar nos nodes do Godot como "components" no estilo Unity/ECS — eles **não funcionam assim**. Nodes são parte de uma árvore e a maioria funciona **independentemente** uns dos outros (com exceção de alguns como collision shapes que dependem do pai physics body).

- Nodes herdam de seus pais na hierarquia até `Node` — são objetos OOP, não componentes injetáveis.

### 3.3 O Editor é um Jogo Godot

- O editor do Godot roda no próprio engine — usa o sistema de UI do engine, pode hot-reload código e scenes.
- **Regra**: Use a anotação `@tool` no topo de qualquer arquivo GDScript para executá-lo no editor.

```gdscript
@tool
extends Node

# Este script executa dentro do editor Godot
func _ready():
    print("Rodando no editor!")
```

- Com `@tool` é possível criar plugins, editores de nível customizados, importers/exporters, usando a mesma API usada nos jogos.

> ⚠ Evite: Tentar importar o editor como um projeto Godot típico — ele é compilado em C++ estaticamente no binário e não possui `project.godot`.

### 3.4 Motores 2D e 3D Separados

- Godot possui motores de renderização 2D e 3D **dedicados e separados**.
- **Regra**: Em scenes 2D, a unidade base é **pixels**.
- É possível renderizar 2D em 3D, 3D em 2D, e sobrepor sprites/UI 2D sobre o mundo 3D.

> ⚠ Evite: Usar o workspace 3D para trabalhos que exigem ferramentas avançadas (terrains, animação complexa de personagens) sem plugins externos — o workspace 3D tem menos ferramentas integradas do que o 2D.

---

## 5. Workflow: Criando e Executando Scenes

### 5.1 Criar uma Scene

- Na dock **Scene** (esquerda), use **Add Child Node** para adicionar o primeiro node.
- Atalhos rápidos no editor vazio: **2D Scene** → `Node2D`; **3D Scene** → `Node3D`; **User Interface** → `Control`.
- O diálogo "Create New Node" permite digitar o nome do node para filtrar a lista.
- **Regra**: Salve a scene antes de executar — o editor solicita automaticamente. Arquivo salvo como `.tscn`.
- O prefixo `res://` representa a **raiz do projeto** (resource path); o editor só permite salvar arquivos dentro de `res://`.

### 5.2 Executar Scenes

| Ação | Tecla (Win/Linux) | Tecla (macOS) |
|---|---|---|
| Rodar scene atual | `F6` | `Cmd + R` |
| Encerrar scene | `F8` | `Cmd + .` |
| Rodar projeto (main scene) | `F5` | `Cmd + B` |

- **Run Current Scene** roda apenas a scene aberta no editor.
- **Run Project** roda a main scene configurada no projeto.
- Ao usar **Run Project** pela primeira vez, Godot pede para selecionar a main scene; a escolha é salva em `project.godot` na raiz do projeto.
- Configurações do projeto também editáveis via **Project > Project Settings**.

> ⚠ Evite: Confundir "Run Current Scene" com "Run Project" — eles rodam scenes diferentes.

---

## 4. Referência de Classe Integrada

- **Atalho principal**: `F1` em qualquer lugar do editor (macOS: `Opt + Space`; laptops: `Fn + F1`).
- `Ctrl + Click` (macOS: `Cmd + Click`) sobre nome de classe, função ou variável no editor de script abre a documentação diretamente.
- Clique direito em nodes → "Open Documentation" abre a referência da classe.
- **Regra**: Prefira navegar a referência **offline dentro do editor** a usar a versão online — é mais rápido e contextual.

A referência de classe documenta para cada classe:
- Hierarquia de herança (com links para classes pai)
- Propriedades, métodos, signals, enums e constantes
- Links para páginas do manual com mais detalhes

---

## 6. Instancing de Scenes

### 6.1 O que é Instancing

- Scenes salvas como `.tscn` são chamadas de **Packed Scenes** — funcionam como blueprints/templates.
- **Instancing** = reproduzir um objeto a partir de um template de scene. Cada instância é uma cópia independente.
- Instâncias exibem apenas o node raiz no editor (conteúdo interno oculto por padrão).
- Cada instância tem um **nome único** na árvore, mas compartilha a estrutura e propriedades padrão da packed scene.
- Alterações na packed scene original propagam para **todas** as instâncias (exceto propriedades sobrescritas localmente).

### 6.2 Instancear no Editor

| Ação | Método |
|---|---|
| Adicionar instância como filho | Selecionar node pai → ícone de link no topo da dock Scene |
| Duplicar instância existente | `Ctrl+D` (macOS: `Cmd+D`) |

- Após instanciar, mova a instância arrastando no viewport.
- Cada instância pode ter suas propriedades modificadas individualmente no **Inspector**.

### 6.3 Editar Instances vs Scene-Template

- **Modificar a scene-template** (abrir o `.tscn` e alterar o node): todas as instâncias do projeto atualizam automaticamente ao salvar.
- **Modificar uma instância** no Inspector: sobrescreve apenas aquela instância — um ícone de "revert" cinza indica o override.
  - Clicar no ícone restaura o valor da packed scene original.
  - O override é preservado mesmo que a scene-template seja alterada depois.
- **Regra**: Mudança em propriedade de instância **sempre** sobrescreve o valor da packed scene correspondente.

> ⚠ Evite: Tentar editar um **Resource** (ex.: `PhysicsMaterial`) diretamente numa instância sem antes fazer "Make Unique". Resources compartilhados precisam ser tornados únicos via clique direito → **Make Unique** no Inspector — do contrário a edição afetaria todas as instâncias que compartilham o resource.

### 6.4 Scenes como Linguagem de Design

- **Regra**: Ao projetar um jogo em Godot, abandone padrões arquiteturais como MVC ou diagramas ER — projete baseado nos **elementos visíveis para o jogador**.
- Crie um diagrama onde cada retângulo = uma entidade visível no jogo; setas apontam para quem instancia cada scene.
- Crie uma scene para cada elemento do diagrama; use instancing (editor ou código) para construir a árvore de scenes.
- Essa abordagem reduz a necessidade de código arquitetural abstrato: a maioria dos componentes do jogo mapeia diretamente para uma scene.

**Exemplo — estrutura de shooter:**
```
Game
 ├── HUD (UI overlay)
 ├── World
 │    ├── Environment
 │    ├── Player
 │    └── Enemies
 │         └── Enemy (múltiplas instâncias)
 └── ...
```

**Exemplo — open-world aninhado:**
```
World
 └── Citadel (instâncias de House)
      └── House (instâncias de Room)
           └── Room (com furniture)
```

**Resumo — o que Instancing oferece:**
- Dividir o jogo em **componentes reutilizáveis**
- Ferramenta para estruturar e encapsular sistemas complexos
- Linguagem natural para pensar sobre a estrutura do projeto de jogo

---

## 7. Primeiro Script GDScript

### 7.1 Estrutura de um Script

- Todo arquivo `.gd` é implicitamente uma classe.
- `extends NodeType` — define qual classe o script herda; sem `extends`, herda `RefCounted` por padrão.
- Scripts herdam **todas** as propriedades e funções do node ao qual estão anexados (incluindo as classes pai do node).
- **Regra**: Anexe um script a um node clicando com o botão direito → "Attach Script" → escolha template "Object: Empty" para começar limpo.
- Convenção de nomes: arquivos `.gd` em `snake_case`; arquivos `.cs` em `PascalCase` (nome do arquivo = nome da classe).

```gdscript
extends Sprite2D

# variáveis membro aqui (após extends, antes das funções)
var speed = 400
var angular_speed = PI
```

- `_init()` é o **construtor** — chamado pelo engine ao criar o objeto em memória.
- `Ctrl+Click` (macOS: `Cmd+Click`) em qualquer propriedade ou função no script editor abre a documentação da classe.

> 💡 Nota: Propriedades no Inspector são exibidas em "Title Case", mas no código são `snake_case`. Hover sobre a propriedade no Inspector mostra o nome correto.

### 7.2 Variáveis Membro e _process

- **Variáveis membro** ficam no topo do script, após `extends`, antes das funções — cada instância do node tem sua própria cópia.
- **Variáveis locais** (dentro de funções) existem apenas no escopo da função.
- `_process(delta)` — virtual function chamada **a cada frame**; `delta` = tempo em segundos desde o último frame.
- **Regra**: Multiplique sempre por `delta` para movimento/rotação independente de framerate.

```gdscript
func _process(delta):
    rotation += angular_speed * delta
```

- `rotation` é herdado de `Node2D` — valor em **radianos**.
- `PI` é uma constante embutida do GDScript.

> ⚠ Evite: Acumular valores por frame sem multiplicar por `delta` — o comportamento dependerá do FPS da máquina.

### 7.3 Movimento com Vector2

- `Vector2.UP` — constante: vetor apontando para cima `(0, -1)`.
- `Vector2.ZERO` — constante: vetor nulo `(0, 0)`.
- `.rotated(angle)` — rotaciona um vetor pelo ângulo em radianos.
- `position` é herdado de `Node2D` — tipo `Vector2`.

```gdscript
func _process(delta):
    rotation += angular_speed * delta
    var velocity = Vector2.UP.rotated(rotation) * speed
    position += velocity * delta
```

> 💡 Nota: Este movimento não detecta colisões. Para movimento com física, use `CharacterBody2D` e `move_and_slide()`.

---

## 8. Input do Jogador

### 8.1 Input Singleton vs Callbacks

Dois modos principais de processar input:

| Modo | Quando usar |
|---|---|
| `Input` singleton (em `_process`) | Input contínuo a cada frame (mover, virar) |
| `_unhandled_input(event)` | Eventos únicos (pular, atirar, confirmar) |

- **`Input` singleton** é um objeto globalmente acessível — use-o dentro de `_process()` para verificar teclas pressionadas continuamente.

### 8.2 Ações de Input

- `Input.is_action_pressed("action_name")` — retorna `true` enquanto a ação está pressionada.
- Ações predefinidas em todo projeto Godot: `ui_left`, `ui_right`, `ui_up`, `ui_down`, `ui_accept`, `ui_cancel`.
- **Configurar ações customizadas**: Project > Project Settings > **Input Map**.

```gdscript
func _process(delta):
    var direction = 0
    if Input.is_action_pressed("ui_left"):
        direction = -1
    if Input.is_action_pressed("ui_right"):
        direction = 1
    rotation += angular_speed * direction * delta

    var velocity = Vector2.ZERO
    if Input.is_action_pressed("ui_up"):
        velocity = Vector2.UP.rotated(rotation) * speed
    position += velocity * delta
```

---

## 9. Usando Signals

### 9.1 Conectar Signal no Editor

- `Signal` é um **tipo first-class** desde Godot 4.0 — pode ser passado como argumento sem usar strings.
- Para conectar no editor: selecionar o node emissor → aba "**Signals**" (ao lado do Inspector) → double-click no signal → escolher node receptor → Create.
- Convenção de nome para callback: `_on_NomeDoNode_nome_do_signal` (GDScript) / `OnNomeDoNodeNomeDoSignal` (C#).

```gdscript
# gerado automaticamente ao conectar Button "pressed" ao Sprite2D
func _on_button_pressed():
    set_process(not is_processing())
```

- `Node.set_process(bool)` — ativa/desativa o processamento do node (para `_process`).
- `Node.is_processing()` — retorna `true` se o node está processando.

> ⚠ Evite: Usar strings para referenciar signals ao conectar via código no Godot 4 — use referência direta ao signal (ex.: `timer.timeout.connect(callback)`).

### 9.2 Conectar Signal via Código

- Conecte signals no `_ready()` — chamado automaticamente quando o node está totalmente instanciado.
- `get_node("NomeDoNode")` — obtém referência a um node filho pelo nome; se renomear o node no editor, atualize a string.
- Sintaxe: `signal_reference.connect(callback_function)`.

```gdscript
func _ready():
    var timer = get_node("Timer")
    timer.timeout.connect(_on_timer_timeout)

func _on_timer_timeout():
    visible = not visible
```

- `visible` — propriedade booleana herdada de `CanvasItem`; controla visibilidade do node.
- Node `Timer` com `Autostart = true` começa a contar imediatamente ao entrar na cena.

> 💡 Nota: Use `get_node()` via código quando nodes são criados/instanciados dinamicamente em scripts — não é possível conectar via editor o que não existe em design time.

### 9.3 Signals Customizados

- Declare com `signal nome_do_signal` no topo do script (após `extends`).
- Emita com `nome_do_signal.emit()`.
- Signals com argumentos: declare os parâmetros; emita passando valores.
- **Regra**: Nomeie signals com **verbo no passado** — representam eventos que acabaram de ocorrer (ex.: `health_depleted`, `enemy_died`).

```gdscript
extends Node2D

signal health_depleted
signal health_changed(old_value, new_value)

var health = 10

func take_damage(amount):
    var old_health = health
    health -= amount
    health_changed.emit(old_health, health)
    if health <= 0:
        health_depleted.emit()
```

- Signals customizados aparecem na aba "Signals" do editor e podem ser conectados como os embutidos.

> 💡 Nota: O número de argumentos ao emitir fica a seu critério — o editor usa a declaração para gerar callbacks, mas não impede emitir mais ou menos argumentos.

---

## 10. Tutorial: Jogo 2D Completo (Dodge the Creeps)

Tutorial de referência: "Dodge the Creeps!" — jogo onde o personagem desvia de inimigos. Cobre setup, Player, Mob, Main scene, HUD e polimento.

### 10.1 Setup do Projeto

- **Modo portrait**: Project Settings → Display → Window → Viewport Width: `480`, Viewport Height: `720`.
- **Stretch**: Mode = `canvas_items`, Aspect = `keep` — garante escala consistente em telas de tamanhos diferentes.
- **Estrutura de scenes**: criar 3 scenes independentes — `Player`, `Mob` e `HUD` — combinadas na `Main` scene.
- **Regra**: Para jogos pequenos, salvar scenes e scripts na raiz `res://` é suficiente.

Convenções de nomes:

| Linguagem | Classes/Nodes | Variáveis/Funções | Constantes |
|---|---|---|---|
| GDScript | `PascalCase` | `snake_case` | `ALL_CAPS` |
| C# | `PascalCase` | `camelCase` / `_camelCase` (private) | — |

### 10.2 Scene do Player (Area2D)

- **Regra**: O root node de uma scene deve refletir a funcionalidade do objeto. Player usa `Area2D` para detectar colisões e overlaps.
- Adicionar `CollisionShape2D` **após** configurar os visuals (`AnimatedSprite2D`) para dimensionar a hitbox com precisão.
- `AnimatedSprite2D` requer um resource `SpriteFrames` — crie-o no Inspector ("New SpriteFrames") e adicione as animações nele.
- **Regra**: Use o botão "Groups" no topo da dock Scene para agrupar o node pai com seus filhos — impede seleção acidental de filhos ao clicar no viewport 2D/3D.
- `CapsuleShape2D` é a forma mais adequada para hitbox de personagem humanóide.
- `hide()` em `_ready()` esconde o player ao iniciar o jogo; `show()` + reset de posição é feito pela função `start(pos)` chamada pela Main.

### 10.3 Script do Player

- **`@export var`**: expõe a variável ao Inspector; valor editado no Inspector sobrescreve o padrão do script (o script não é modificado).
- **`$NomeDoNode`**: shorthand para `get_node("NomeDoNode")` — retorna `null` se o node não existir; nomes são case-sensitive.
- **Normalização de velocity**: sempre normalize o vetor de direção antes de multiplicar pela velocidade — previne movimento diagonal mais rápido que horizontal/vertical.

```gdscript
extends Area2D

signal hit
@export var speed = 400
var screen_size

func _ready():
    screen_size = get_viewport_rect().size
    hide()

func _process(delta):
    var velocity = Vector2.ZERO
    if Input.is_action_pressed("move_right"): velocity.x += 1
    if Input.is_action_pressed("move_left"):  velocity.x -= 1
    if Input.is_action_pressed("move_down"):  velocity.y += 1
    if Input.is_action_pressed("move_up"):    velocity.y -= 1

    if velocity.length() > 0:
        velocity = velocity.normalized() * speed
        $AnimatedSprite2D.play()
    else:
        $AnimatedSprite2D.stop()

    position += velocity * delta
    position = position.clamp(Vector2.ZERO, screen_size)

    # Flip sprite baseado na direção
    if velocity.x != 0:
        $AnimatedSprite2D.animation = "walk"
        $AnimatedSprite2D.flip_h = velocity.x < 0
        $AnimatedSprite2D.flip_v = false
    elif velocity.y != 0:
        $AnimatedSprite2D.animation = "up"
        $AnimatedSprite2D.flip_v = velocity.y > 0

func _on_body_entered(_body):
    hide()
    hit.emit()
    $CollisionShape2D.set_deferred("disabled", true)

func start(pos):
    position = pos
    show()
    $CollisionShape2D.disabled = false
```

- `flip_h` e `flip_v` espelham o sprite — evite criar animações separadas para direções opostas.
- **`set_deferred("disabled", true)`**: use em vez de atribuição direta ao desativar `CollisionShape2D` dentro de um callback de colisão — Godot aguarda o momento seguro para aplicar a mudança.

> ⚠ Evite: Desativar `CollisionShape2D.disabled` diretamente dentro de um callback de física — causa erro. Use sempre `set_deferred`.

### 10.4 Scene do Mob (RigidBody2D)

- `Gravity Scale = 0`: desativa gravidade no RigidBody2D — o mob se move apenas pela `linear_velocity` definida no script.
- Collision Mask: desmarcar layer 1 → mobs não colidem entre si.
- `Array.pick_random()`: seleciona item aleatório de um Array (GDScript).
- **`queue_free()`**: agenda a exclusão do node ao final do frame atual — método seguro para auto-deletar.
- **`VisibleOnScreenNotifier2D`**: emite `screen_exited` quando o node sai da tela; conecte ao `queue_free()` para limpeza automática.

```gdscript
extends RigidBody2D

func _ready():
    var mob_types = Array($AnimatedSprite2D.sprite_frames.get_animation_names())
    $AnimatedSprite2D.animation = mob_types.pick_random()
    $AnimatedSprite2D.play()

func _on_visible_on_screen_notifier_2d_screen_exited():
    queue_free()
```

### 10.5 Main Scene e Spawning

- **Regra**: Use `Node` (não `Node2D`) como root da Main scene quando o node é um container de lógica sem necessidade de posicionamento 2D.
- **`@export var mob_scene: PackedScene`**: permite atribuir a scene do mob pelo Inspector (arrastar `.tscn` ou "Load").
- **`Path2D` + `PathFollow2D`**: defina um caminho fechado na borda da tela; `progress_ratio = randf()` seleciona um ponto aleatório no caminho para spawn.

> ⚠ Evite: Desenhar o `Path2D` no sentido anti-horário — mobs spawnham virados para fora. Sempre desenhe **no sentido horário**.

- **`add_child(mob)`**: obrigatório para adicionar instância criada via código à scene.
- **`get_tree().call_group("mobs", "queue_free")`**: deleta todos os nodes do grupo `"mobs"` — use no início de `new_game()` para limpar inimigos da partida anterior.
- **`randf_range(min, max)`**: número float aleatório no intervalo — varie a velocidade dos mobs para evitar monotonia.

```gdscript
extends Node

@export var mob_scene: PackedScene
var score

func _on_mob_timer_timeout():
    var mob = mob_scene.instantiate()
    var mob_spawn_location = $MobPath/MobSpawnLocation
    mob_spawn_location.progress_ratio = randf()
    mob.position = mob_spawn_location.position
    var direction = mob_spawn_location.rotation + PI / 2
    direction += randf_range(-PI / 4, PI / 4)
    mob.rotation = direction
    mob.linear_velocity = Vector2(randf_range(150.0, 250.0), 0.0).rotated(direction)
    add_child(mob)

func new_game():
    get_tree().call_group("mobs", "queue_free")
    score = 0
    $Player.start($StartPosition.position)
    $StartTimer.start()

func game_over():
    $ScoreTimer.stop()
    $MobTimer.stop()
```

Timers da Main scene:

| Timer | Wait Time | One Shot |
|---|---|---|
| MobTimer | 0.5s | Off |
| ScoreTimer | 1s | Off |
| StartTimer | 2s | On |

### 10.6 HUD (CanvasLayer)

- **`CanvasLayer`**: renderiza UI em layer acima de todos os elementos do jogo — UI não é coberta por sprites ou mobs.
- **`await $Timer.timeout`**: pausa a execução do script até o timer terminar (corrotina GDScript).
- **`get_tree().create_timer(1.0).timeout`**: cria um timer one-shot temporário sem precisar de node `Timer` na scene — ideal para delays pontuais.
- **Anchors** de Control nodes: definem o ponto de referência das bordas do node; use "Anchor Presets" para posicionamento rápido.
- Fontes customizadas: "Theme Overrides > Fonts" → Load; tamanho em "Theme Overrides > Font Sizes".
- **`Shortcut`** no Button: crie um `InputEventAction` apontando para uma input action — permite iniciar o jogo pelo teclado além do clique.
- **`AudioStreamPlayer`**: nomes sugeridos `Music` e `DeathSound`; para loop de música, abrir o Stream → "Make Unique" → marcar "Loop".

```gdscript
extends CanvasLayer

signal start_game

func show_message(text):
    $Message.text = text
    $Message.show()
    $MessageTimer.start()

func show_game_over():
    show_message("Game Over")
    await $MessageTimer.timeout
    $Message.text = "Dodge the Creeps!"
    $Message.show()
    await get_tree().create_timer(1.0).timeout
    $StartButton.show()

func update_score(score):
    $ScoreLabel.text = str(score)

func _on_start_button_pressed():
    $StartButton.hide()
    start_game.emit()

func _on_message_timer_timeout():
    $Message.hide()
```

- **Polimento**: adicionar `ColorRect` (background colorido) ou `TextureRect` (imagem) como **primeiro filho** da Main — garante que seja desenhado atrás dos demais nodes.

---

## 11. Tutorial: Jogo 3D Completo (Squash the Creeps)

Tutorial de referência: "Squash the Creeps!" — jogo 3D onde o personagem pula sobre monstros para esmagá-los. Cobre setup 3D, CharacterBody3D, câmera ortográfica, physics layers, pulo, squash, hitbox, score, retry e animações.

### 11.1 Setup da Área de Jogo 3D

- **Regra**: Use `Node` (sem sufixo 2D/3D) como root da Main scene quando for apenas um container de lógica.
- **Chão**: `StaticBody3D` renomeado para `Ground` → filho `CollisionShape3D` com `BoxShape3D` (tamanho 60×2×60) → filho `MeshInstance3D` com `BoxMesh` (mesmo tamanho).
- Mova o `Ground` -1 unidade no eixo Y para deixar a grade do editor visível. Filhos se movem junto.
- **Luz direcional**: adicione `DirectionalLight3D` à Main; mova para cima e gire no eixo X até iluminar o chão; ative **Shadow** no Inspector.
- **Regra**: Use **grid snap** (`Y` ou botão de ímã) ao posicionar nodes no viewport 3D para precisão.
- Resolução padrão do tutorial: **720×540** (Project Settings → Display → Window).

### 11.2 Scene do Player 3D (CharacterBody3D)

- **Root node**: `CharacterBody3D` → renomeie para `Player`.
- **Rig de modelo**: adicione `Node3D` filho → renomeie para `Pivot`; arraste `player.glb` do FileSystem para dentro de `Pivot` (renomeie o modelo para `Character`).
  - `Pivot` permite rotacionar o modelo via código sem interferir na física do `CharacterBody3D`.
- **Hitbox**: adicione `CollisionShape3D` como filho de `Player` com `SphereShape3D` (radius ~0.8 m); alinhe a base da esfera com o plano do chão.
- `.glb` = glTF 2.0 — formato aberto, moderno; alternativa ao FBX. Godot importa ambos.
- **Input Map** (Project → Project Settings → Input Map): crie as ações `move_left`, `move_right`, `move_forward`, `move_back`, `jump`. Vincule teclas de seta, WASD e joystick analógico esquerdo + botão A para `jump`.

> 💡 Nota: Para suporte a gamepad por slot, use a opção **Devices** no Input Map — Device 0 = primeiro joystick conectado.

### 11.3 Movimento 3D e Câmera

- **Regra**: Use `_physics_process(delta)` (não `_process`) para todo código de movimento com `CharacterBody3D` — executa em intervalos fixos, projetado para física.
- No plano 3D, o chão é o **plano XZ** (não XY como em 2D). O eixo Y aponta para cima.
- **Rotação para a direção de movimento**: `$Pivot.basis = Basis.looking_at(direction)` — gira o Pivot para olhar na direção do vetor de movimento normalizado.

```gdscript
extends CharacterBody3D

@export var speed = 14
@export var fall_acceleration = 75
var target_velocity = Vector3.ZERO

func _physics_process(delta):
    var direction = Vector3.ZERO
    if Input.is_action_pressed("move_right"): direction.x += 1
    if Input.is_action_pressed("move_left"):  direction.x -= 1
    if Input.is_action_pressed("move_back"):  direction.z += 1
    if Input.is_action_pressed("move_forward"): direction.z -= 1

    if direction != Vector3.ZERO:
        direction = direction.normalized()
        $Pivot.basis = Basis.looking_at(direction)

    target_velocity.x = direction.x * speed
    target_velocity.z = direction.z * speed
    if not is_on_floor():
        target_velocity.y -= fall_acceleration * delta

    velocity = target_velocity
    move_and_slide()
```

- `is_on_floor()` — retorna `true` se o corpo colidiu com o chão neste frame.
- `move_and_slide()` — usa a propriedade `velocity` nativa do `CharacterBody3D`; suaviza colisões com paredes.

**Câmera ortográfica (recomendada para este estilo de jogo):**
- Estrutura: `Marker3D` (`CameraPivot`) → `Camera3D`.
- Mova `Camera3D` ~19 unidades no eixo Z; gire `CameraPivot` -45° no eixo X para câmera "em grua".
- Inspector da câmera: `Projection = Orthogonal`, `Size = 19`.
- **Regra**: Com câmera ortográfica, reduza `Far` (ex.: 100) se as sombras direcionais ficarem muito borradas.

> 💡 Nota: Use `Ctrl+2` (macOS: `Cmd+2`) para dividir o viewport 3D em dois — um para navegação livre, outro para preview da câmera.

### 11.4 Scene do Mob 3D

- **Root**: `CharacterBody3D` → `Mob`; filho `Node3D` → `Pivot`; arraste `mob.glb` para `Pivot` → `Character`.
- Hitbox: `CollisionShape3D` com `BoxShape3D` ajustada ao modelo.
- **Regra**: A hitbox não precisa ser perfeita — o que importa é como o jogo se sente ao testar. Prefira hitbox levemente menor que o modelo para parecer justa ao jogador.
- `VisibleOnScreenNotifier3D`: conecte o signal `screen_exited` → `queue_free()` para auto-deletar mobs fora da tela.
- **GDScript não precisa de object pooling** — usa contagem de referências (não garbage collector), então instanciar/deletar é eficiente.

Função `initialize` do Mob (chamada pela Main ao spawnar):

```gdscript
extends CharacterBody3D

@export var min_speed = 10
@export var max_speed = 18
signal squashed

func _physics_process(_delta):
    move_and_slide()

func initialize(start_position, player_position):
    look_at_from_position(start_position, player_position, Vector3.UP)
    rotate_y(randf_range(-PI / 4, PI / 4))
    var random_speed = randi_range(min_speed, max_speed)
    velocity = Vector3.FORWARD * random_speed
    velocity = velocity.rotated(Vector3.UP, rotation.y)

func squash():
    squashed.emit()
    queue_free()

func _on_visible_on_screen_notifier_3d_screen_exited():
    queue_free()
```

- `look_at_from_position(pos, target, up)` — posiciona e orienta o node para olhar em direção ao target.
- `Vector3.FORWARD * speed` + `.rotated(Vector3.UP, rotation.y)` — transforma velocidade local em velocidade no mundo.

### 11.5 Spawn Path e Spawning 3D

- **Regra**: Use cilindros `MeshInstance3D` como placeholders visuais ao desenhar caminhos de spawn no viewport 3D — eles mostram os limites do campo de visão da câmera.
- Estrutura de spawn: `Path3D` (renomeado `SpawnPath`) → `PathFollow3D` (renomeado `SpawnLocation`).
  - Desenhe o `Path3D` ao redor das bordas do viewport usando a câmera de preview como guia.
  - `progress_ratio = randf()` seleciona ponto aleatório no caminho (0.0 = início, 1.0 = fim).

> ⚠ Evite: Desenhar o `Path3D` no sentido anti-horário em 3D — pode orientar mobs incorretamente.

Spawning via `Timer` (Wait Time: 0.5s, Autostart: On):

```gdscript
extends Node

@export var mob_scene: PackedScene

func _on_mob_timer_timeout():
    var mob = mob_scene.instantiate()
    var mob_spawn_location = get_node("SpawnPath/SpawnLocation")
    mob_spawn_location.progress_ratio = randf()
    var player_position = $Player.position
    mob.initialize(mob_spawn_location.position, player_position)
    add_child(mob)
    mob.squashed.connect($UserInterface/ScoreLabel._on_mob_squashed.bind())
```

### 11.6 Physics Layers, Pulo e Squash

**Nomeando layers** (Project Settings → Layer Names → 3D Physics): `player` (1), `enemies` (2), `world` (3).

| Node | Layer | Mask |
|---|---|---|
| Ground | world (3) | — (sem mask) |
| Player | player (1) | enemies + world |
| Mob | enemies (2) | — (sem mask) |

- Mobs com mask vazia atravessam uns aos outros — ajuste conforme a mecânica desejada.

**Pulo** (adicionar ao Player):

```gdscript
@export var jump_impulse = 20

# dentro de _physics_process, antes de move_and_slide:
if is_on_floor() and Input.is_action_just_pressed("jump"):
    target_velocity.y = jump_impulse
```

- `Input.is_action_just_pressed` — detecta apenas o frame em que a ação foi pressionada (ideal para pulo, não para movimento contínuo).

**Squash** — detectar colisão com mob vindo de cima:

```gdscript
@export var bounce_impulse = 16

for index in range(get_slide_collision_count()):
    var collision = get_slide_collision(index)
    if collision.get_collider() == null:
        continue
    if collision.get_collider().is_in_group("mob"):
        var mob = collision.get_collider()
        if Vector3.UP.dot(collision.get_normal()) > 0.1:
            mob.squash()
            target_velocity.y = bounce_impulse
            break
```

- `get_slide_collision_count()` / `get_slide_collision(i)` — enumera todas as colisões do `move_and_slide()` neste frame.
- `Vector3.UP.dot(collision.get_normal()) > 0.1` — dot product > 0 significa ângulo < 90° entre vetores; valor > 0.1 confirma que o player está acima do mob.
- **Regra**: Use grupos (`is_in_group("mob")`) para distinguir tipos de colisão em vez de verificar tipos de node diretamente.
- **Regra**: Após processar squash, use `break` para evitar chamadas duplicadas a `mob.squash()` no mesmo frame.
- Adicione a tag `"mob"` ao node Mob via **dock Groups** no editor.

### 11.7 Morte do Player e Hitbox (Area3D)

- **Regra**: Use `Area3D` para hitbox de dano recebido — permite detectar colisões laterais separadamente das colisões físicas de chão/parede do `CharacterBody3D`.
- Estrutura: `Area3D` filho (`MobDetector`) → `CollisionShape3D` com `CylinderShape3D`.
  - Reduza a altura do cilindro e eleve-o para que fique inativo quando o player estiver no ar (só mata no chão).
  - Largura do cilindro > esfera do player → player é atingido antes de montar no mob.
- `MobDetector`: desative **Monitorable** (não detectável por outros); mantenha **Monitoring** ativo; Layer = nenhuma, Mask = enemies.
- Conecte o signal `body_entered` do `MobDetector` ao Player:

```gdscript
signal hit

func die():
    hit.emit()
    queue_free()

func _on_mob_detector_body_entered(body):
    die()
```

- Na Main, conecte o signal `hit` do Player → pare o `MobTimer`:

```gdscript
func _on_player_hit():
    $MobTimer.stop()
```

### 11.8 Score, Retry e Autoload

**Score**: `Control` (UserInterface) → `Label` (ScoreLabel). Script no ScoreLabel:

```gdscript
extends Label
var score = 0

func _on_mob_squashed():
    score += 1
    text = "Score: %s" % score
```

- Conecte via código ao spawnar: `mob.squashed.connect($UserInterface/ScoreLabel._on_mob_squashed.bind())`.
- `"Score: %s" % score` — formatação de string GDScript; converte automaticamente para texto.

**Retry overlay**: `ColorRect` filho de `UserInterface`, com `Anchor Preset → Full Rect`; cor escura semi-transparente (canal A baixo). Filho `Label` centralizado com "Press Enter to retry.".

```gdscript
func _ready():
    $UserInterface/Retry.hide()

func _on_player_hit():
    $MobTimer.stop()
    $UserInterface/Retry.show()

func _unhandled_input(event):
    if event.is_action_pressed("ui_accept") and $UserInterface/Retry.visible:
        get_tree().reload_current_scene()
```

- `get_tree().reload_current_scene()` — reinicia a scene atual completamente.
- `_unhandled_input(event)` — callback para eventos únicos que não foram consumidos por outros nodes.

**Autoload (música contínua)**:
- Crie scene com `AudioStreamPlayer` (Autoplay = On), salve como `music_player.tscn`.
- Registre em Project Settings → **Globals → Autoload** — a scene carrega automaticamente em qualquer scene do projeto.
- **Regra**: Use Autoload para objetos que devem persistir entre recarregamentos de scene (música, save data, singletons de jogo).

> 💡 Nota: O **Remote** tab na dock Scene (durante o jogo em execução) mostra a árvore de nodes ao vivo — inclui autoloads no topo, acima da Main scene.

### 11.9 Animação 3D (AnimationPlayer)

- Adicione `AnimationPlayer` como filho do `Player`; crie animação "float" (duração 1.2s, Loop On, Autoplay On).
- Anime propriedades do node `Character` (filho de `Pivot`): `Position.Y` e `Rotation.X` com keyframes em tempos diferentes para criar efeito de flutuação.
- **Regra**: Anime o `Character` (modelo), não o `Player` ou `Pivot` — preserva a capacidade de mover o personagem via código sem conflito com a animação.
- **Easing curves**: selecione keyframes → Inspector → propriedade `Easing`. Ease-out = transição rápida que desacelera (curva para a esquerda). Varie entre keyframes para movimento orgânico.
- **Regra**: Não distribua keyframes uniformemente — offset e contraste entre tempos tornam o movimento mais vivo.

**Controlar velocidade de animação via código**:

```gdscript
# em _physics_process, após checar direction:
if direction != Vector3.ZERO:
    $AnimationPlayer.speed_scale = 4
else:
    $AnimationPlayer.speed_scale = 1

# arc de pulo — ao final de _physics_process:
$Pivot.rotation.x = PI / 6 * velocity.y / jump_impulse
```

- `speed_scale` — multiplica a velocidade de reprodução da animação (1.0 = normal).
- Rotacionar o `Pivot` no eixo X durante o pulo cria arco visual sem modificar a animação.

**Reutilizar animação nos Mobs**:
- Animações podem ser copiadas entre scenes com estrutura similar (AnimationPlayer → Animation → Manage Animations → Copy/Paste).
- Sincronize `speed_scale` com `random_speed / min_speed` no `initialize()` do Mob para mobs mais rápidos animarem mais rápido.

---

## 12. Boas Práticas

### 12.1 Organização de Scenes (Loose Coupling)

- **Regra**: Projete scenes sem dependências externas — tudo que precisam deve estar dentro delas.
- **Regra**: Quando uma scene precisa interagir com contexto externo, use **Dependency Injection** — exponha propriedades e deixe o pai configurar as dependências. Quatro opções (da mais segura à menos):
  1. **Signal** — responder a comportamentos (nomes no passado: `entered`, `item_collected`)
  2. **NodePath** exportada — `@export var target_path: NodePath`; o filho chama `get_node(target_path)`
  3. **Referência de Node** exportada — `@export var target: Node`
  4. **Callable** exportada — `@export var func_property: Callable`; o filho chama `func_property.call()`
- **Regra**: Nodes irmãos só devem conhecer a própria hierarquia — use um ancestral como mediador entre eles.

```gdscript
# Pai: medeia comunicação entre Left e Right
$Left.target = $Right.get_node("Receiver")

# Left: depende apenas de uma propriedade injetada
var target: Node
func execute():
    # usa target
```

- `_get_configuration_warnings()` — retorne `PackedStringArray` com mensagens de erro; aparece como ícone de aviso na dock Scene para auto-documentar dependências faltantes.

> ⚠ Evite: Hard-coded `get_node("../SiblingNode")` em scripts de scenes reutilizáveis — impede reuso e quebra ao mover a scene na árvore.

### 12.2 Estrutura da Node Tree

Estrutura recomendada de Main scene:

```
Node "Main" (main.gd)
  ├── Node2D/Node3D "World" (game_world.gd)
  └── Control "GUI" (gui.gd)
```

- **Regra**: Use parent-child apenas quando a remoção do pai faz sentido para os filhos. Se um node pode existir independentemente, coloque-o como sibling ou em ramo próprio.
- **Regra**: Use `RemoteTransform` / `RemoteTransform2D` para que nodes separados mantenham posição relativa entre si sem depender de hierarquia.
- Para herdar posição de um pai mas isolar o transform de um filho: use `Node` intermediário (sem transform) ou ative a propriedade `top_level` em `CanvasItem` ou `Node3D`.
- Em jogos maiores, mantenha o player em ramo separado da SceneTree (não dentro de "Room") — evita "casos especiais" que exigem documentação para a equipe.

> 💡 Nota: Para sistemas de dados globais com escopo amplo (quests, save, singletons de jogo), crie um node Autoload registrado em Project Settings → Globals → Autoload.

### 12.3 Scene vs Script

- **Script** (`.gd`) sem scene: use para ferramentas reutilizáveis em múltiplos projetos ou quando precisa de `class_name` para aparecer no diálogo de criação do editor.
- **Scene** (`.tscn`): use para conceitos específicos do jogo — mais fácil de editar e mais segura que código puro.
- **Performance**: `PackedScene` é processada em batch pelo engine (C++); scripts são mais lentos por passarem pela scripting API. Quanto mais complexo o node, mais razão para usar scene em vez de script.

```gdscript
# Namespace: script com class_name que expõe uma scene como constante
class_name Game
extends RefCounted  # não aparece no diálogo de nodes

const MyScene = preload("my_scene.tscn")

# Uso em outro script:
add_child(Game.MyScene.instantiate())
```

### 12.4 Autoload — Quando Usar (e Quando Não Usar)

- **Regra**: Prefira nodes com estado interno à propria scene — cada scene gerencia seu estado, acessa apenas seus nodes e aloca exatamente os recursos que precisa.
- **Quando usar Autoload**: sistemas de escopo amplo que gerenciam dados próprios sem interferir em outros objetos (ex.: sistema de quests, sistema de diálogos, música persistente entre scenes).
- **Quando NÃO usar Autoload**: sons, lógica de personagem, qualquer dado que pertença naturalmente a uma scene.
- `static func` + `class_name` — bibliotecas de helpers sem precisar de instância.
- `static var` (Godot 4.1+) — compartilha variáveis entre instâncias sem autoload.

> ⚠ Evite: "Sound manager global" — cria global state, global access e alocação de pool imprecisa. Prefira `AudioStreamPlayer` embutido em cada scene que precisa de áudio.

### 12.5 Objetos Não-Node (Object, RefCounted, Resource)

Use quando nodes têm overhead desnecessário para dados puros:

| Tipo | Gerenciamento | Uso ideal |
|---|---|---|
| `Object` | Manual (`.free()`) | Estruturas de dados customizadas (ex.: árvorezinhas) |
| `RefCounted` | Automático (ref-count) | A maioria das classes de dados customizadas |
| `Resource` | Automático + serialização | Dados que precisam do Inspector ou de salvar em disco |

- **Regra**: Use `Object`/`RefCounted`/`Resource` em vez de `Node` para dados puros — Node inclui transform, grupos e sinais de ciclo de vida que não serão usados.

```gdscript
class_name TreeNode
extends Object

var _parent: TreeNode = null
var _children := []

func _notification(p_what):
    match p_what:
        NOTIFICATION_PREDELETE:
            for child in _children:
                child.free()
```

### 12.6 Interfaces e Aquisição de Referências

Formas de acessar nodes em GDScript, da mais lenta à mais rápida:

| Método | Notas |
|---|---|
| `get_node("Child")` | Lookup dinâmico por string — evite em `_process` |
| `$Child` | Alias de `get_node` — mesmo custo |
| `@onready var child = $Child` | Cache no `_ready()` — acesso rápido depois |
| `@export var child: Node` | Mais rápido + configurável no Inspector |

- **Duck typing**: GDScript verifica métodos/propriedades em runtime. Use `has_method()`, `is_in_group()` ou `is` para verificações seguras antes de chamar.
- **Regra**: Use grupos como "interfaces implícitas" — qualquer node no grupo `"quest"` deve implementar os métodos documentados do grupo.

```gdscript
@onready var child = $Child  # rápido; não quebra se node se mover depois

# duck-typed: verificar antes de chamar
if child.has_method("set_visible"):
    child.set_visible(false)

# cast check: múltiplas chamadas seguras
if child is CanvasItem:
    child.set_visible(false)
    child.show_on_top = true
```

> ⚠ Evite: Chamar `get_node()` dentro de `_process()` a cada frame — cache a referência em `_ready()` com `@onready`.

### 12.7 Notificações e Lifecycle

| Callback | Quando usar |
|---|---|
| `_init()` | Inicializar propriedades; construir sub-tree sem scene |
| `_enter_tree()` | Node entrou na SceneTree (filhos ainda não prontos) |
| `_ready()` | Node e todos os filhos prontos — acesso seguro a `$Child` |
| `_process(delta)` | Lógica framerate-dependente; verificações recorrentes |
| `_physics_process(delta)` | Movimento físico — framerate-independente, consistente |
| `*_input(event)` | Eventos únicos — só dispara quando há input real |
| `NOTIFICATION_PARENTED` | Reagir ao ser adicionado a um pai, mesmo fora da main scene |

- **Regra**: Use `*_input()` para eventos únicos (pular, confirmar) — não executa quando não há input, economizando processamento.
- **Regra**: Use `Timer.timeout` em vez de lógica em `_process()` para operações que não precisam executar todo frame.

Sequência de inicialização para propriedades `@export`:
1. Valor inicial do script (sem chamar o setter)
2. `_init()` — chama o setter
3. Valor configurado no Inspector — chama o setter novamente

```gdscript
# Útil para data-nodes criados em runtime: reage ao ser parented sem estar na main scene
func _notification(what):
    match what:
        NOTIFICATION_PARENTED:
            parent_cache = get_parent()
            if parent_cache.has_user_signal("interacted_with"):
                parent_cache.interacted_with.connect(_on_parent_interacted_with)
        NOTIFICATION_UNPARENTED:
            if parent_cache.has_user_signal("interacted_with"):
                parent_cache.interacted_with.disconnect(_on_parent_interacted_with)
```

### 12.8 Preferências de Dados

| Estrutura | Melhor para | Evitar para |
|---|---|---|
| `Array` | Iteração, acesso por índice, listas ordenadas | Inserções/remoções frequentes no início |
| `Dictionary` | Lookup por chave, insert/erase O(1) | Busca por valor |
| `Object` | Controle, signals, abstrações complexas | Dados simples (use Array/Dictionary) |

- Array: inserção/remoção eficiente apenas no **final**; para muitas operações no início, inverta o array, opere no final, inverta novamente.
- **Enum**: prefira `int` para performance (comparação O(1)); use string enum com `@export_enum` apenas quando precisa imprimir valores legíveis diretamente.

**Escolha de sistema de animação:**

| Necessidade | Ferramenta |
|---|---|
| Spritesheet 2D simples | `AnimatedSprite2D` + `SpriteFrames` |
| Textura animada em loop (tiles) | `AnimatedTexture` |
| Transforms, propriedades, partículas, funções | `AnimationPlayer` |
| Blending entre animações, máquinas de estado | `AnimationTree` |

### 12.9 Preferências de Lógica

- **Regra**: Configure todas as propriedades do node **antes** de `add_child()` — setters fora da SceneTree são mais eficientes; dentro da árvore podem disparar atualizações caras.
- **`preload()` vs `load()`**: use `preload()` para constantes (carrega junto com o script); use `load()` para variáveis e recursos que podem ser substituídos ou descarregados.

```gdscript
const EnemyScn = preload("res://enemy.tscn")  # carrega ao iniciar o script
var office_scn = load("res://office.tscn")    # carrega quando a linha executa
```

> ⚠ Evite: `const X = load(...)` — `load` é runtime e não pode inicializar constantes. Use `preload`.

- **Nível estático vs dinâmico**: jogos pequenos → nível estático; jogos médios/grandes → carregamento e descarregamento dinâmico de scenes para controlar uso de memória.

### 12.10 Organização do Projeto

Estrutura de diretórios recomendada:

```
/project.godot
/docs/.gdignore
/models/town/house/house.glb
/characters/player/player.tscn
/characters/enemies/goblin/goblin.tscn
/levels/riverdale/riverdale.tscn
/addons/third_party_plugin/
```

Convenções de nomenclatura:

| Tipo | Convenção |
|---|---|
| Pastas e arquivos `.gd` | `snake_case` |
| Scripts C# (`.cs`) | `PascalCase` |
| Nomes de nodes no editor | `PascalCase` |
| Assets e plugins de terceiros | pasta `addons/` na raiz |

- `.gdignore` — arquivo vazio em uma pasta impede Godot de importar seus conteúdos e oculta a pasta no FileSystem dock.

> ⚠ Evite: Misturar maiúsculas/minúsculas em nomes de arquivo — Windows é case-insensitive, Linux e o PKC virtual são case-sensitive; causa erros ao exportar.

### 12.11 VCS (Git)

Adicione ao `.gitignore` (Godot 4.1+):

```
.godot/
*.translation
```

- **Regra**: No Windows, configure `git config --global core.autocrlf input` para evitar que arquivos Godot sejam marcados como modificados por diferença de line endings.
- **Regra**: Configure Git LFS **antes** do primeiro commit de binários — migrar depois é complexo.

Exemplo de `.gitattributes` para Git LFS:

```
* text=auto eol=lf

*.glb  filter=lfs diff=lfs merge=lfs -text
*.png  filter=lfs diff=lfs merge=lfs -text
*.jpg  filter=lfs diff=lfs merge=lfs -text
*.ogg  filter=lfs diff=lfs merge=lfs -text
*.wav  filter=lfs diff=lfs merge=lfs -text
*.mp3  filter=lfs diff=lfs merge=lfs -text
*.ttf  filter=lfs diff=lfs merge=lfs -text
*.scn  filter=lfs diff=lfs merge=lfs -text
*.res  filter=lfs diff=lfs merge=lfs -text
```

> 💡 Nota: Project Manager → New Project → opção Git gera `.gitignore` e `.gitattributes` automaticamente. Em projetos existentes: Project menu → Version Control → Generate Version Control Metadata.

---

## 13. GDScript Avançado

### 13.1 @export — Variantes e Agrupamentos

`@export` salva a propriedade junto à scene e a exibe no Inspector. O valor definido no Inspector sobrescreve o padrão do script (sem modificar o script).

**Tipos básicos:**
```gdscript
@export var speed: int = 400
@export var label: Label          # node
@export var texture: Texture2D    # resource
```

**Variantes úteis:**

| Anotação | Comportamento |
|---|---|
| `@export_range(min, max)` | Slider numérico no Inspector |
| `@export_range(0, 10, 0.1)` | Com passo |
| `@export_enum("Idle", "Walk", "Run")` | Dropdown de opções |
| `@export_file("*.tscn")` | String com seletor de arquivo |
| `@export_flags("Fire", "Water", "Earth")` | Bitmask de flags |
| `@export_flags_2d_physics` | Bitmask de layers de física 2D |
| `@export_multiline` | Campo de texto multi-linha |
| `@export_color_no_alpha` | Color picker sem canal alpha |

**Agrupamento no Inspector:**
```gdscript
@export_group("Combat")
@export var attack: int = 10
@export var defense: int = 5

@export_subgroup("Advanced")
@export var crit_chance: float = 0.1
```

- `@export_group("")` — encerra o grupo e volta ao topo.
- `@export_category("My Category")` — cria nova categoria na lista; use com cuidado para não quebrar a hierarquia do Inspector.
- **Regra**: Propriedades exportadas com getters/setters só executam os setters/getters dentro do editor quando o script usa `@tool`.

> 💡 Nota: Para documentação (tooltip ao hover), use um comentário de documentação imediatamente antes do `@export`:
> ```gdscript
> ## Velocidade do personagem em pixels/s.
> @export var speed: float = 400.0
> ```

### 13.2 Tipagem Estática (Static Typing)

- Vantagens: detecção de erros antes de executar, autocomplete completo, melhor performance (opcodes otimizados em tempo de compilação).
- **Regra**: Ative "Text Editor > Completion > Add Type Hints" nas configurações do editor para tipo-hints automáticos.

**Declaração:**
```gdscript
var damage: float = 10.5         # tipo explícito
var speed := 14.0                # tipo inferido (float)
const MAX_SPEED: float = 50.0

func sum(a: float, b: float) -> float:
    return a + b

func _process(delta: float) -> void:
    pass
```

- `:=` infere o tipo do valor à direita — use para variáveis locais.
- `-> void` indica que a função não retorna valor.

**Arrays tipados:**
```gdscript
var scores: Array[int] = [10, 20, 30]
var items: Array[Item] = []
# for-loop herda o tipo:
for score in scores:
    print(score + 1)  # score é int
```

**Tipos customizados como hint:**
```gdscript
# Opção 1: preload em constante
const Rifle = preload("res://player/weapons/rifle.gd")
var my_rifle: Rifle

# Opção 2: class_name no arquivo-fonte (registra globalmente)
# Em rifle.gd:
class_name Rifle
extends Node2D
# Em qualquer outro script:
var my_rifle: Rifle
```

**Covariância / Contravariância** (herança de métodos):
```gdscript
class_name Parent
func get_prop(param: Label) -> Node: ...

class_name Child extends Parent
# param pode ser supertipo (Control > Label); retorno pode ser subtipo (Node2D < Node)
func get_prop(param: Control) -> Node2D: ...
```

> ⚠ Evite: Tentar usar `Array[Array[int]]` (arrays de arrays tipadas não são suportados). Use `Array[Array]`.

### 13.3 Format Strings

Três formas de formatar strings em GDScript:

```gdscript
# 1. Operador % (mais comum)
"Pontos: %d" % score
"Pos: (%.1f, %.1f)" % [x, y]

# 2. String.format()
"Pontos: {0}".format([score])
"Olá, {name}!".format({"name": "Godot"})

# 3. Concatenação simples
"Pontos: " + str(score)
```

**Especificadores do operador `%`:**

| Especificador | Tipo esperado | Exemplo |
|---|---|---|
| `%s` | Qualquer (via str()) | `"Valor: %s" % true` → `"Valor: True"` |
| `%d` | Inteiro | `"HP: %d" % 42` |
| `%f` | Float (6 casas decimais) | `"%.2f" % 3.14159` → `"3.14"` |
| `%v` | Vector (qualquer) | `"%v" % Vector2(1,2)` → `"(1, 2)"` |
| `%x` / `%X` | Hexadecimal | `"%x" % 255` → `"ff"` |
| `%%` | Literal `%` | `"100%%"` → `"100%"` |

**Padding e alinhamento:**
```gdscript
"%5d"  % 42       # "   42"  (pad com espaço à esquerda)
"%-5d" % 42       # "42   "  (pad à direita)
"%05d" % 42       # "00042"  (pad com zero)
"%.3f" % 3.14159  # "3.142"  (3 casas decimais)
```

---

## 14. Física

### 14.1 Tipos de Collision Objects

Godot oferece 4 tipos de collision objects (todos estendem `CollisionObject2D` / `CollisionObject3D`):

| Tipo | Movido pela física? | Uso típico |
|---|---|---|
| `Area2D` / `Area3D` | Não | Detectar overlaps, zonas de efeito, trigger |
| `StaticBody2D` / `StaticBody3D` | Não | Chão, paredes, plataformas |
| `RigidBody2D` / `RigidBody3D` | Sim (simulado) | Objetos com física realista (pedras, caixas) |
| `CharacterBody2D` / `CharacterBody3D` | Não (código) | Personagens controlados pelo jogador |

- **Regra**: Todo collision object precisa de pelo menos um nó `CollisionShape2D`/`CollisionShape3D` filho para detectar colisões.
- **Regra**: Nunca escale collision shapes pelo transform (Scale no Inspector deve ser 1,1). Use sempre os handles de tamanho da forma.
- **`PhysicsMaterial`**: pode ser atribuído a `StaticBody` e `RigidBody` para controlar friction, bounce, absorbent e rough.

**`_physics_process(delta)`** — use para todo código que interage com física. Executa em taxa fixa (padrão 60 Hz), diferente de `_process` (taxa variável de frame).

### 14.2 Collision Layers e Masks

Cada `CollisionObject` tem 32 layers de física:

| Propriedade | Significado |
|---|---|
| `collision_layer` | Em quais layers o objeto **existe** |
| `collision_mask` | Quais layers o objeto **detecta** |

- **Regra**: Nomeie as layers em Project Settings → Layer Names → 2D/3D Physics para facilitar manutenção.
- **Regra**: Se um objeto não precisa colidir com outro, remova-o da mask — economiza CPU.

```gdscript
# Via código: habilitar layers específicas (mais legível)
$CollisionObject.set_collision_layer_value(1, true)   # layer "player"
$CollisionObject.set_collision_mask_value(2, true)    # detecta layer "enemies"

# Export para bitmask no Inspector:
@export_flags_2d_physics var physics_layers
```

**Exemplo de configuração:**

| Node | Layer | Mask |
|---|---|---|
| Ground (StaticBody) | world (3) | — |
| Player (CharacterBody) | player (1) | enemies + world |
| Enemy (CharacterBody) | enemies (2) | world |
| Coin (Area2D) | coins (4) | player |

### 14.3 CharacterBody: Movimento e Colisão

`CharacterBody` não é movido pela física — todo movimento é por código. Dois métodos de movimento:

| Método | Retorno | Uso |
|---|---|---|
| `move_and_collide(velocity * delta)` | `KinematicCollision2D` ou `null` | Controle total da resposta à colisão |
| `move_and_slide()` | — | Desliza automaticamente em paredes e rampas |

**Regra**: Use `move_and_slide()` para a maioria dos personagens de plataforma/top-down. Use `move_and_collide()` quando precisar de resposta customizada (ricochetear bala, etc.).

```gdscript
extends CharacterBody2D

var speed = 300
var gravity = 980

func _physics_process(delta):
    # Aplicar gravidade manualmente
    if not is_on_floor():
        velocity.y += gravity * delta

    # Input
    var dir = Input.get_axis("move_left", "move_right")
    velocity.x = dir * speed

    move_and_slide()  # usa a propriedade `velocity` do CharacterBody
```

**Propriedades relevantes de `move_and_slide`:**
- `velocity` — vetor de velocidade (atualizado pelo engine após cada slide)
- `motion_mode` — `MOTION_MODE_GROUNDED` (plataformas) ou `MOTION_MODE_FLOATING` (top-down/espaço)
- `up_direction` — define o que é "chão" (padrão: `Vector2.UP`)
- `floor_max_angle` — ângulo máximo que ainda é considerado chão (padrão: 45°)

**Detectar colisões após `move_and_slide`:**
```gdscript
move_and_slide()
for i in get_slide_collision_count():
    var col = get_slide_collision(i)
    if col.get_collider().is_in_group("enemy"):
        take_damage()
```

**`move_and_collide` com resposta customizada:**
```gdscript
var col = move_and_collide(velocity * delta)
if col:
    # Ricochetear
    velocity = velocity.bounce(col.get_normal())
```

- `is_on_floor()` — true se colidiu com chão neste frame
- `is_on_wall()` — true se colidiu com parede
- `is_on_ceiling()` — true se colidiu com teto
- **Regra**: `Input.is_action_just_pressed("jump")` para pulo (detects apenas o frame de pressão); `Input.is_action_pressed` para movimento contínuo.

> ⚠ Evite: Mover `CharacterBody` via `position` direto — bypassa física e não detecta colisões.

---

## 15. Grupos, Resources e Save Game

### 15.1 Grupos

Grupos funcionam como **tags** — um node pode pertencer a múltiplos grupos.

**Adicionar ao grupo:**
```gdscript
func _ready():
    add_to_group("guards")
    add_to_group("enemies")
```

Ou via editor: dock Scene → selecionar node → botão Groups (+).

**Operações na SceneTree:**
```gdscript
# Chamar método em todos os nodes do grupo
get_tree().call_group("guards", "enter_alert_mode")

# Obter lista de nodes
var guards = get_tree().get_nodes_in_group("guards")

# Verificar pertencimento (em código de colisão)
if body.is_in_group("enemy"):
    take_damage()
```

- **Regra**: Use grupos como "interfaces implícitas" — qualquer node no grupo `"quest"` deve implementar os métodos documentados do grupo (ver seção 12.6).
- **Global Groups** (Project Settings → Globals → Groups): reutilizáveis em qualquer scene; mesma lógica que grupos locais — a distinção é apenas organizacional.

### 15.2 Resources

**Resources são contêineres de dados** — não têm comportamento próprio. Nodes usam os dados contidos em Resources.

- Quando o engine carrega um resource de disco, **carrega uma única cópia** — múltiplas referências ao mesmo `.tres`/`.res` apontam para o mesmo objeto em memória.
- Tipos comuns: `Texture2D`, `AudioStream`, `Font`, `Mesh`, `AnimationLibrary`, `PackedScene`, `Script`.

**Carregar resources via código:**
```gdscript
# load() — carrega em runtime (pode usar variáveis)
var texture = load("res://player.png")

# preload() — carrega em compile-time (somente constantes string)
const PlayerScene = preload("res://player.tscn")
```

**PackedScene (instanciar scenes via código):**
```gdscript
const BulletScene = preload("res://bullet.tscn")

func shoot():
    var bullet = BulletScene.instantiate()
    add_child(bullet)
```

**Resources customizados:**
```gdscript
# bot_stats.gd
class_name BotStats
extends Resource

@export var health: int = 100
@export var speed: float = 200.0

func _init(p_health = 100, p_speed = 200.0):
    health = p_health
    speed = p_speed
```

- `class_name` registra o tipo globalmente — aparece no diálogo "Create Resource" do Inspector.
- Salvar/carregar automaticamente via Inspector (`.tres` = texto, `.res` = binário).
- **Regra**: Prefira `Resource` a `Dictionary` para dados estruturados — recebe getters/setters, signals, serialização automática e edição no Inspector.

> ⚠ Evite: Editar um resource compartilhado diretamente numa instância — afeta todas as instâncias que o compartilham. Use "Make Unique" no Inspector ou `resource.duplicate()` em código antes de modificar.

### 15.3 Save Game (JSON + FileAccess)

Padrão recomendado: marcar nodes persistentes com grupo `"Persist"`, serializar via JSON, salvar em `user://`.

**Salvar:**
```gdscript
func save_game():
    var save_file = FileAccess.open("user://savegame.save", FileAccess.WRITE)
    for node in get_tree().get_nodes_in_group("Persist"):
        if node.scene_file_path.is_empty():
            continue  # ignorar nodes que não são scenes instanciadas
        if not node.has_method("save"):
            continue
        var data = node.call("save")
        save_file.store_line(JSON.stringify(data))
```

**Cada node "Persist" implementa `save()`:**
```gdscript
func save() -> Dictionary:
    return {
        "filename": get_scene_file_path(),
        "parent": get_parent().get_path(),
        "pos_x": position.x,
        "pos_y": position.y,
        "health": health,
        "score": score,
    }
```

**Carregar:**
```gdscript
func load_game():
    if not FileAccess.file_exists("user://savegame.save"):
        return

    # Limpar nodes persistentes existentes antes de carregar
    for node in get_tree().get_nodes_in_group("Persist"):
        node.queue_free()

    var save_file = FileAccess.open("user://savegame.save", FileAccess.READ)
    while save_file.get_position() < save_file.get_length():
        var json = JSON.new()
        if json.parse(save_file.get_line()) != OK:
            continue
        var data = json.data

        var obj = load(data["filename"]).instantiate()
        get_node(data["parent"]).add_child(obj)
        obj.position = Vector2(data["pos_x"], data["pos_y"])
        for key in data.keys():
            if key in ["filename", "parent", "pos_x", "pos_y"]:
                continue
            obj.set(key, data[key])
```

- `user://` → pasta de dados do usuário (`%APPDATA%/Godot/app_userdata/<projeto>` no Windows).
- `res://` → raiz do projeto (somente leitura em builds exportadas).
- **JSON vs binary**: JSON (`.save`) é legível e debugável; use `var_to_bytes()` / `bytes_to_var()` para serialização binária compacta.

> 💡 Nota: Para configurações do usuário (controles, volume, idioma), prefira `ConfigFile` a JSON manual — tem API de seções/chaves e suporta todos os tipos Variant nativamente.

---

## 16. Animação Avançada

### 16.1 AnimationPlayer — Keyframes e Tracks

`AnimationPlayer` pode animar **qualquer propriedade** de qualquer node: posição, rotação, cor, visibilidade, variáveis de script, chamadas de função.

**Setup básico:**
1. Adicione `AnimationPlayer` como filho do node que será animado.
2. Selecione `AnimationPlayer` → painel Animation → botão "New Animation".
3. Selecione o node-alvo → use os botões de chave (🔑) na toolbar ou `Ctrl+K` para criar keyframes.

**Tipos de track:**

| Track | Uso |
|---|---|
| Normal (Property) | Anima qualquer propriedade (position, scale, color, etc.) |
| Transform (Pos/Rot/Scale 3D) | Otimizado para transforms 3D |
| Call Method | Chama função em keyframe específico |
| Audio Playback | Reproduz AudioStream num instante |
| Animation Playback | Controla outro AnimationPlayer |

**Modos de Update (por track):**
- `Continuous` — interpola entre keyframes a cada frame (padrão)
- `Discrete` — aplica apenas no frame do keyframe (útil para animações de sprite frame-a-frame)
- `Capture` — captura o valor atual antes do primeiro keyframe e faz blend até ele

**Modos de Loop:**
```gdscript
# Via código:
var anim = $AnimationPlayer.get_animation("walk")
anim.loop_mode = Animation.LOOP_LINEAR    # loop normal
anim.loop_mode = Animation.LOOP_PINGPONG  # vai-e-volta
anim.loop_mode = Animation.LOOP_NONE      # sem loop
```

**Controle via código:**
```gdscript
$AnimationPlayer.play("walk")
$AnimationPlayer.play_backwards("walk")
$AnimationPlayer.pause()
$AnimationPlayer.stop()
$AnimationPlayer.speed_scale = 2.0      # 2x velocidade
$AnimationPlayer.current_animation      # nome da animação atual

# Autoplay: marcar no editor ou:
$AnimationPlayer.autoplay = "idle"
```

**Signal útil:**
```gdscript
$AnimationPlayer.animation_finished.connect(_on_animation_finished)

func _on_animation_finished(anim_name: String):
    if anim_name == "death":
        queue_free()
```

- **Regra**: Anime o modelo (ex.: `Character`), não o nó de física (ex.: `Player` / `CharacterBody3D`) — preserva a capacidade de mover via código sem conflito com a animação.

> ⚠ Evite: Usar `AnimationPlayer` como filho de `Node2D`/`Node3D` — herança de transform inconsistente. `AnimationPlayer` herda de `Node` sem transform.

### 16.2 AnimationTree — Blending e StateMachine

`AnimationTree` adiciona **blending e máquinas de estado** às animações do `AnimationPlayer`.

**Setup:**
1. Crie `AnimationTree` na scene.
2. Atribua o `AnimationPlayer` em `Tree Root` → `anim_player` no Inspector.
3. Defina `Tree Root` (tipo de root node):
   - `AnimationNodeStateMachine` — para máquinas de estado (personagens com idle/walk/run/jump)
   - `AnimationNodeBlendTree` — para grafo de blending customizado
   - `AnimationNodeBlendSpace2D` — para blend baseado em posição 2D (ex.: direção de movimento)

**Tipos de nós de blend:**

| Nó | Uso |
|---|---|
| `AnimationNodeAnimation` | Referencia uma animação do AnimationPlayer |
| `Blend2` / `Blend3` | Blend por parâmetro 0–1 entre 2 ou 3 animações |
| `OneShot` | Executa animação uma vez e retorna |
| `StateMachine` | Máquina de estados com transições |
| `BlendSpace1D` / `BlendSpace2D` | Blend por posição em espaço 1D/2D |
| `TimeScale` | Multiplica velocidade de reprodução |
| `Transition` | Versão simplificada de StateMachine |

**Controle via código (usar `parameters/` path):**
```gdscript
# Blend2: definir peso de blend (0.0 a 1.0)
$AnimationTree["parameters/Blend2/blend_amount"] = 0.5

# StateMachine: navegar para estado
$AnimationTree["parameters/StateMachine/playback"].travel("run")

# OneShot: disparar
$AnimationTree["parameters/Attack/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

# BlendSpace2D: definir posição de blend
$AnimationTree["parameters/BlendSpace2D/blend_position"] = Vector2(input_x, input_y)
```

**StateMachine — Tipos de transição:**
- `Immediate` — muda de estado imediatamente
- `Sync` — muda imediatamente mas sincroniza o tempo de reprodução
- `At End` — aguarda o término da animação atual antes de mudar

**Advance Condition vs Advance Expression:**
```
# Advance Condition: checa se variável booleana é true
is_walking

# Advance Expression: qualquer expressão (Godot 4)
velocity.length() > 10
is_on_floor() && jump_pressed
```

- **Regra**: Prefira `AnimationTree` a `AnimationPlayer` puro quando o personagem tem mais de 2–3 animações que precisam de transições suaves ou condicionais.
- **Regra**: `AnimationTree` não contém animações próprias — sempre aponta para um `AnimationPlayer` que as contém.

---

## 17. Interface Gráfica (UI / Control)

### 17.1 Anchors e Tamanho de Controls

Cada `Control` possui 4 offsets (left, right, top, bottom) que definem a posição de suas bordas. Os **anchors** (0.0–1.0) determinam o ponto de referência desses offsets dentro do pai: 0.0 = início (topo/esquerda), 1.0 = fim (baixo/direita), 0.5 = centro.

- Definir dois anchors opostos com valores diferentes faz o control **redimensionar junto com o pai**.
- **Regra**: Use anchor 0.5 nos quatro lados + offsets negativos iguais à metade do tamanho do control para centralizá-lo no pai.

```gdscript
# Centralizar TextureRect no pai
rect.anchor_left   = 0.5; rect.anchor_right  = 0.5
rect.anchor_top    = 0.5; rect.anchor_bottom = 0.5
var sz = rect.texture.get_size()
rect.offset_left   = -sz.x / 2;  rect.offset_right  = sz.x / 2
rect.offset_top    = -sz.y / 2;  rect.offset_bottom = sz.y / 2
```

- **Anchor Presets** (toolbar acima do viewport → menu Anchor) fornecem atalhos para alinhamentos e redimensionamentos comuns — preferir ao ajuste manual.
- Offset negativo coloca a borda **antes** do ponto de anchor (p. ex., acima/à esquerda do centro).

### 17.2 Containers

Quando um `Control` é filho de um `Container`, ele **perde controle sobre o próprio posicionamento** — qualquer ajuste manual é ignorado ou sobrescrito ao redimensionar.

**Sizing options** (Inspector → Layout de filhos de Container):

| Opção | Efeito |
|---|---|
| `Fill` | Preenche a área designada pelo container (padrão: ativo) |
| `Expand` | Usa o máximo de espaço disponível no eixo do container |
| `Shrink Begin/Center/End` | Alinhamento dentro do espaço expandido |
| `Stretch Ratio` | Proporção de espaço entre controls que usam `Expand` |

**Tipos de Container integrados:**

| Container | Uso |
|---|---|
| `HBoxContainer` / `VBoxContainer` | Filhos em linha horizontal ou vertical |
| `GridContainer` | Grid com número fixo de colunas |
| `MarginContainer` | Adiciona padding nas bordas (valor vem do Theme) |
| `TabContainer` | Pilha de controls, um visível por aba |
| `HSplitContainer` / `VSplitContainer` | Dois filhos separados por divisor arrastável |
| `PanelContainer` | Desenha `StyleBox` e expande filhos sobre ela |
| `FoldableContainer` | Expansível/colapsável; oculta filhos ao colapsar |
| `ScrollContainer` | Adiciona scrollbars se o filho exceder o tamanho |
| `AspectRatioContainer` | Preserva proporções ao redimensionar |
| `HFlowContainer` / `VFlowContainer` | Filhos quebram para próxima linha/coluna ao atingir limite |
| `CenterContainer` | Centraliza filhos no tamanho mínimo deles |
| `SubViewportContainer` | Exibe um `Viewport` como imagem |

**Container customizado** — responde a `NOTIFICATION_SORT_CHILDREN`:
```gdscript
extends Container

func _notification(what):
    if what == NOTIFICATION_SORT_CHILDREN:
        for c in get_children():
            fit_child_in_rect(c, Rect2(Vector2(), size))

func set_some_setting():
    queue_sort()  # força re-layout dos filhos
```

- **Regra**: Chame `queue_sort()` sempre que uma propriedade que afeta o layout dos filhos mudar.

### 17.3 Controls Customizados

**Desenho** — em `_draw()`, use `size` para manter o conteúdo dentro dos bounds:
```gdscript
func _draw():
    if has_focus():
        draw_selected()   # mostrar indicador visual de foco
    else:
        draw_normal()
```

**Tamanho mínimo** — necessário para layout correto em Containers:
```gdscript
func _get_minimum_size() -> Vector2:
    return Vector2(30, 30)

# Alternativa imperativa:
func _ready():
    set_custom_minimum_size(Vector2(30, 30))
```

**Input** — `_gui_input(event)` recebe eventos apenas quando:
1. O ponteiro do mouse está sobre o control, **ou**
2. O botão foi pressionado sobre o control (captura até soltar), **ou**
3. O control tem foco de teclado/joypad (`focus_mode ≠ None`).

```gdscript
func _gui_input(event):
    if event is InputEventMouseButton \
            and event.button_index == MOUSE_BUTTON_LEFT \
            and event.pressed:
        print("clique esquerdo")
```

**Notifications úteis em controls customizados:**

| Notification | Quando ocorre |
|---|---|
| `NOTIFICATION_MOUSE_ENTER` | Mouse entrou na área do control |
| `NOTIFICATION_MOUSE_EXIT` | Mouse saiu da área |
| `NOTIFICATION_FOCUS_ENTER` | Control ganhou foco |
| `NOTIFICATION_FOCUS_EXIT` | Control perdeu foco |
| `NOTIFICATION_THEME_CHANGED` | Theme do control foi alterado — redesenhar |
| `NOTIFICATION_VISIBILITY_CHANGED` | Control ficou visível/invisível |
| `NOTIFICATION_RESIZED` | Tamanho do control mudou |

### 17.4 Navegação por Teclado e Gamepad (Focus)

Todo `Control` pode receber foco. Por padrão, alguns nodes (ex.: `Button`) respondem às ações `ui_up`, `ui_down`, `ui_focus_next`, etc.

**Focus mode** (Inspector → Control → Focus → Mode):

| Modo | Comportamento |
|---|---|
| `All` | Foco por clique do mouse ou navegação teclado/joypad |
| `Click` | Foco somente por clique do mouse |
| `None` | Sem foco (padrão em `Label`, por exemplo) |

- **Focus neighbors** (Inspector → Control → Focus → Neighbor *): define explicitamente o próximo node em cada direção e nas transições Tab/Shift+Tab.
- **Regra**: Sempre defina um node com foco inicial via código ao carregar a scene — sem isso, teclado/gamepad não funcionam.

```gdscript
func _ready():
    $StartButton.grab_focus.call_deferred()
```

- **Regra**: Não use ações `ui_*` de foco (`ui_up`, `ui_down`, etc.) em código de gameplay — são reservadas para navegação de UI.
- Um node perde o foco ao ficar oculto (`hide()`).

> ⚠ Evite: Depender da detecção automática de neighbors pelo engine em UIs complexas — configure `focus_neighbor_*` explicitamente para garantir o fluxo de navegação esperado.

---

## 18. Input Avançado

### 18.1 InputEvent — Tipos e Fluxo de Propagação

`InputEvent` é o tipo base de todos os eventos de input. Eventos percorrem o engine em ordem fixa e param quando consumidos.

**Tipos principais de InputEvent:**

| Tipo | Descrição |
|---|---|
| `InputEventKey` | Tecla pressionada/solta; contém `keycode` e modificadores |
| `InputEventMouseButton` | Clique/scroll; contém `button_index` e `position` |
| `InputEventMouseMotion` | Movimento do mouse; contém `relative`, `velocity`, `position` |
| `InputEventJoypadButton` | Botão de controle digital |
| `InputEventJoypadMotion` | Eixo analógico de controle |
| `InputEventScreenTouch` | Toque em touchscreen (pressionar/soltar) |
| `InputEventScreenDrag` | Arrasto em touchscreen |
| `InputEventAction` | Ação genérica gerada por código |

**Ordem de propagação** (viewport, reverse depth-first):

1. `Node._input()` — qualquer node que sobrescreva; pode chamar `Viewport.set_input_as_handled()` para parar.
2. GUI (`Control._gui_input()`) — consome se o mouse estiver sobre o control ou o control tiver foco.
3. `Node._shortcut_input()` — apenas `InputEventKey`, `InputEventShortcut`, `InputEventJoypadButton`.
4. `Node._unhandled_key_input()` — apenas `InputEventKey`.
5. `Node._unhandled_input()` — tudo que não foi consumido; ideal para input de gameplay.

**Regra**: Use `_unhandled_input()` para input de gameplay — garante que a GUI intercepte primeiro. Use `_input()` apenas quando precisar filtrar antes da GUI.

```gdscript
func _unhandled_input(event):
    if event is InputEventKey:
        if event.pressed and event.keycode == KEY_ESCAPE:
            get_tree().quit()
```

### 18.2 Teclado e Mouse

**Teclado — `InputEventKey`:**

```gdscript
func _input(event):
    if event is InputEventKey and event.pressed:
        if event.keycode == KEY_T:
            if event.shift_pressed:
                print("Shift+T")
            else:
                print("T")
```

- Constantes de tecla em `@GlobalScope_Key` (ex.: `KEY_ESCAPE`, `KEY_SPACE`).
- Modificadores: `event.shift_pressed`, `event.ctrl_pressed`, `event.alt_pressed`, `event.meta_pressed`.

> ⚠ Evite: Checar teclas específicas em código de gameplay — use `InputMap` e ações nomeadas para permitir remapping pelo jogador.

**Mouse — botões (`InputEventMouseButton`):**

```gdscript
func _input(event):
    if event is InputEventMouseButton and event.pressed:
        match event.button_index:
            MOUSE_BUTTON_LEFT:
                print("clique esquerdo em ", event.position)
            MOUSE_BUTTON_WHEEL_UP:
                print("scroll up")
```

- Scroll conta como dois botões: `MOUSE_BUTTON_WHEEL_UP` e `MOUSE_BUTTON_WHEEL_DOWN`.

**Mouse — movimento e drag (`InputEventMouseMotion`):**

```gdscript
extends Node

var dragging = false

func _input(event):
    if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
        if (event.position - $Sprite2D.position).length() < 32:
            if not dragging and event.pressed:
                dragging = true
        if dragging and not event.pressed:
            dragging = false
    if event is InputEventMouseMotion and dragging:
        $Sprite2D.position = event.position
```

**Cursor customizado:**

```gdscript
func _ready():
    Input.set_custom_mouse_cursor(load("res://cursor.png"))
    # Para cursor de tipo específico (ex.: I-beam de texto):
    Input.set_custom_mouse_cursor(load("res://beam.png"), Input.CURSOR_IBEAM)
```

- Imagem máxima: 256×256 px (recomendado ≤ 128×128); web: máximo 128×128.
- **Regra**: Prefira cursor de hardware (via `Input.set_custom_mouse_cursor`) ao cursor de software (Sprite2D movido em `_process`) — o software adiciona ao menos 1 frame de latência.

### 18.3 Touch e Coordenadas do Mouse

**Touch (mobile):**

- `InputEventScreenTouch` — equivalente a clique do mouse (press/release).
- `InputEventScreenDrag` — equivalente a movimento do mouse.
- Para testar toque em desktop: Project Settings → Input Devices/Pointing → **Emulate Touch From Mouse**.

**Coordenadas do mouse:**

```gdscript
func _input(event):
    if event is InputEventMouseButton:
        print("clique em: ", event.position)          # coordenadas do viewport
    print("resolução do viewport: ", get_viewport().get_visible_rect().size)

# Posição atual do mouse:
get_viewport().get_mouse_position()
```

- `event.position` usa **coordenadas do viewport**, não do hardware — use sempre estas.

**Mouse em modo capturado (`Input.MOUSE_MODE_CAPTURED`):**

- `event.position` retorna o centro da tela — não use para movimento.
- Use `event.relative` (relativo ao frame anterior) e `event.velocity` para processar movimento.
- Para comportamento consistente entre resoluções: prefira `event.screen_relative` e `event.screen_velocity`.

### 18.4 Gamepads e Controles

**Regra**: Use `InputMap` e ações nomeadas para suportar teclado e controle com o mesmo código — sem caminhos separados.

**Escolha do método do singleton `Input` por tipo de eixo:**

| Situação | Método | Retorno |
|---|---|---|
| 2 eixos (joystick, WASD) | `Input.get_vector(neg_x, pos_x, neg_y, pos_y)` | `Vector2` entre `(-1,-1)` e `(1,1)` |
| 1 eixo bidirecional | `Input.get_axis(neg, pos)` | `float` entre `-1.0` e `1.0` |
| Analog simples (trigger) | `Input.get_action_strength("action")` | `float` entre `0.0` e `1.0` |
| Digital (botão, tecla) | `Input.is_action_pressed("action")` | `bool` |
| Pressionado neste frame | `Input.is_action_just_pressed("action")` | `bool` (true apenas 1 frame) |

```gdscript
func _physics_process(delta):
    var velocity = Input.get_vector("move_left", "move_right", "move_forward", "move_back")
    # get_vector aplica deadzone circular — mais correto que get_axis combinado
```

**Deadzone:** padrão `0.5`; ajustável por ação no InputMap. Em `get_vector()`, passável como 5º parâmetro opcional.

> ⚠ Evite: Usar `Vector2(get_action_strength(...) - get_action_strength(...), ...)` para movimento 2D — o resultado tem deadzone quadrado. Use `get_vector()`.

**Diferenças controle vs teclado/mouse:**

- Controles **não geram echo events** ao manter botão pressionado — simule com `Timer` + `Input.parse_input_event()` se necessário.
- Input de controle é **visível em todas as janelas**, incluindo janelas sem foco. Para ignorar input em janela não focada, crie um autoload `Focus`:

```gdscript
# Focus.gd
extends Node
var focused := true

func _notification(what: int) -> void:
    match what:
        NOTIFICATION_APPLICATION_FOCUS_OUT: focused = false
        NOTIFICATION_APPLICATION_FOCUS_IN:  focused = true

func input_is_action_pressed(action: StringName) -> bool:
    return focused and Input.is_action_pressed(action)
```

- Controles **não impedem economia de energia** (tela apagando). Verifique `Display > Window > Energy Saving > Keep Screen On` nas Project Settings.

**Vibração (haptic feedback):**

```gdscript
# Vibrar fraco por 0.5s e forte por 0.3s
Input.start_joy_vibration(0, 0.3, 0.7, 0.5)
Input.stop_joy_vibration(0)  # parar antes do fim
# Mobile (independente do controle):
Input.vibrate_handheld(500)  # milissegundos
```

> 💡 Nota: Ofereça slider in-game para desativar vibração — pode ser desconfortável para alguns jogadores.

**LED de controle (DualShock/DualSense, desktop apenas):**

```gdscript
func _process(_delta):
    if Input.has_joy_light(0):  # verifica suporte
        Input.set_joy_light(0, Color.RED)
```

### 18.5 Encerramento da Aplicação (Quit)

**Desktop/Web — NOTIFICATION_WM_CLOSE_REQUEST:**

```gdscript
func _notification(what):
    if what == NOTIFICATION_WM_CLOSE_REQUEST:
        get_tree().quit()  # comportamento padrão
```

Para controlar o quit manualmente (ex.: salvar antes de sair):

```gdscript
func _ready():
    get_tree().set_auto_accept_quit(false)  # desativa quit automático

func _notification(what):
    if what == NOTIFICATION_WM_CLOSE_REQUEST:
        _save_game()
        get_tree().quit()
```

**Propagar notificação de quit para todos os nodes** (antes de chamar `quit()`):

```gdscript
get_tree().root.propagate_notification(NOTIFICATION_WM_CLOSE_REQUEST)
get_tree().quit()
```

> ⚠ Evite: Chamar apenas `get_tree().quit()` sem propagar — os nodes não recebem notificação e não podem executar ações de finalização (salvar, confirmar, etc.).

**Mobile — sem equivalente a NOTIFICATION_WM_CLOSE_REQUEST:**

- Use `NOTIFICATION_APPLICATION_PAUSED` para salvar estado quando o app é suspenso.
- iOS: máximo ~5 segundos após pause antes de ser morto pelo OS.
- Android: Back button dispara `NOTIFICATION_WM_GO_BACK_REQUEST` (se `Quit On Go Back` estiver ativo nas Project Settings).

---

## 19. Matemática (Math)

### 19.1 Vetores — Operações Fundamentais

Vetores representam **direção e magnitude relativas** — não posição absoluta. Dois vetores com os mesmos componentes são idênticos independentemente de onde sejam desenhados.

**Tipos Godot**: `Vector2(x, y)` (2D), `Vector3(x, y, z)` (3D). Y aponta para baixo em 2D.

**Operações básicas:**
```gdscript
var c = a + b           # adição de vetores
var d = a - b           # subtração (B - A = vetor de A para B)
var e = a * 2           # multiplicação por scalar (escala; não muda direção se positivo)
position += velocity * delta  # movimento: nova posição = posição atual + velocidade * tempo
```

**Vetores unitários (normalização):**
```gdscript
a = a.normalized()      # comprimento reduzido a 1, direção preservada
# NUNCA normalize vetor de comprimento 0 — em GDScript retorna o vetor intacto
```

**Operações úteis:**
```gdscript
# Vetor de A para B (normalizado):
var dir = A.direction_to(B)

# Refletir velocity em uma superfície com normal col.get_normal():
var col = move_and_collide(velocity * delta)
if col:
    velocity = velocity.bounce(col.get_normal())
```

**Produto escalar (dot product):**
```gdscript
var d = a.dot(b)   # retorna scalar; com vetores unitários = cos(θ)
# d > 0 → ângulo < 90° (mesma direção geral)
# d = 0 → perpendiculares
# d < 0 → ângulo > 90° (direções opostas)

# Detectar se zombie vê o player (campo de visão 180°):
var to_player = zombie.direction_to(player.position)
if to_player.dot(zombie_facing) > 0:
    print("vê o player")
```

**Produto vetorial (cross product — apenas 3D):**
```gdscript
var normal = side1.cross(side2)  # vetor perpendicular à face de um triângulo
# Ordem importa: a.cross(b) ≠ b.cross(a) (direções opostas)
```

> ⚠ Evite: Normalizar vetores de comprimento zero (resultado indefinido). Verifique `length() > 0` antes se necessário.

### 19.2 Planos e Detecção de Colisão (SAT)

Um plano é definido por um vetor normal (N) e distância da origem (D). Godot fornece o tipo `Plane`.

```gdscript
var dist = plane.distance_to(point)   # positivo = lado do normal; negativo = outro lado
var inv   = -plane                    # inverter polaridade do plano
```

**Ponto dentro de polígono convexo:**
```gdscript
var inside = true
for p in planes:
    if p.distance_to(point) > 0:
        inside = false
        break
```

**Separating Axis Theorem (SAT) — colisão entre convexos 2D:**
```gdscript
var overlapping = true
for p in planes_of_A:
    var all_out = true
    for v in points_of_B:
        if p.distance_to(v) < 0:
            all_out = false; break
    if all_out:
        overlapping = false; break
# Repetir testando planes_of_B contra points_of_A
```

- **Regra**: Para polígonos 3D, adicione ao SAT planos gerados pelo produto vetorial das arestas (`ea.cross(eb)`) — necessário para casos onde as faces sozinhas não são suficientes.

> 💡 Nota: O motor de física do Godot já implementa SAT internamente. Use planos manualmente apenas para lógica customizada (hitboxes, zonas, IA).

### 19.3 Transforms e Matrizes

`Transform2D` contém três vetores: `x` (coluna X), `y` (coluna Y) e `origin`. As colunas `x`/`y` formam a **base** (rotação + escala); `origin` = posição.

```
Transform2D identity:
x = (1, 0)   y = (0, 1)   origin = (0, 0)
```

**Escalar:**
```gdscript
t.x *= 2; t.y *= 2           # escala por 2
# Em projetos, prefira: transform = transform.scaled(Vector2(2, 2))
```

**Rotacionar (manual — prefira `rotated()`):**
```gdscript
var rot = 0.5  # radianos
t.x.x = cos(rot);  t.y.y = cos(rot)
t.x.y = sin(rot);  t.y.x = -sin(rot)
# Godot usa Y-para-baixo + sentido horário; a trigonometria funciona igual ao sistema Y-para-cima
```

**Transladar:**
```gdscript
t.origin = Vector2(350, 150)       # posição relativa ao pai
# translated(v)       → move no espaço do pai (global-local)
# translated_local(v) → move relativo à própria orientação
```

**Converter posições entre espaços:**
```gdscript
# Local → mundo:
var world_pos = transform * Vector2(0, 100)
# Mundo → local:
var local_pos = Vector2(0, 100) * transform
```

**Mover relativo a si mesmo (forward/strafe):**
```gdscript
# 2D:
transform.origin += transform.x * 100    # move 100 u para a direita local
# 3D:
transform.origin += transform.basis.x * 100
# ou: translate_object_local(Vector3(100, 0, 0))
```

**Compor transforms (pai × filho = world transform):**
```gdscript
var world = parent_transform * child_transform   # ordem importa!
var identity_check = t.affine_inverse() * t      # sempre → identity
```

**3D:**
- `Transform3D` = `Basis` (3×3: x, y, z) + `origin` (Vector3).
- Rotação 3D: use `Basis` ou `Quaternion` — evite Euler angles para uso geral.
- `TAU` = 2π radianos (volta completa); `PI/2` = 90°.

> ⚠ Evite: Multiplicar transforms em ordem errada — `parent * child` ≠ `child * parent`.

### 19.4 Interpolação (Lerp)

`lerp(a, b, t)` = `a + (b - a) * t` — t=0 retorna A, t=1 retorna B, velocidade constante.

```gdscript
# Mover de A para B ao longo do tempo:
var t = 0.0
func _physics_process(delta):
    t += delta * 0.4
    $Sprite2D.position = $A.position.lerp($B.position, t)

# Interpolação de transforms completos:
$Monkey.transform = $P1.transform.interpolate_with($P2.transform, t)
```

**Smooth follow — framerate-dependente (seguro em `_physics_process`):**
```gdscript
const FOLLOW_SPEED = 4.0
func _physics_process(delta):
    position = position.lerp(target_pos, delta * FOLLOW_SPEED)
```

**Smooth follow — framerate-independente (seguro em `_process` também):**
```gdscript
const FOLLOW_SPEED = 4.0
func _process(delta):
    var weight = 1 - exp(-FOLLOW_SPEED * delta)
    position = position.lerp(target_pos, weight)
```

- **Regra**: Use `1 - exp(-speed * delta)` como peso de lerp em `_process()` para smooth follow framerate-independente. O método `delta * speed` funciona em `_physics_process()` (delta constante) mas é frame-dependente em `_process()`.
- `cubic_interpolate()` — interpolação suave estilo Bezier entre dois pontos com tangentes.

### 19.5 Curvas Bezier e Caminhos

Bezier quadrático: 3 pontos. Bezier cúbico: 4 pontos (`p0`, `p1`, `p2`, `p3`).

```gdscript
func _cubic_bezier(p0: Vector2, p1: Vector2, p2: Vector2, p3: Vector2, t: float) -> Vector2:
    var q0 = p0.lerp(p1, t);  var q1 = p1.lerp(p2, t);  var q2 = p2.lerp(p3, t)
    var r0 = q0.lerp(q1, t);  var r1 = q1.lerp(q2, t)
    return r0.lerp(r1, t)
```

- Bezier com `t` uniforme **não** percorre a curva em velocidade constante.
- **Para velocidade constante**: use `curve.sample_baked(t * curve.get_baked_length(), true)`.
- **Para desenho**: use `Curve2D.tessellate()` — gera segmentos adaptativos (mais onde há curvatura).
- Godot: `Curve2D`/`Curve3D` com `Path2D`/`Path3D` + `PathFollow2D`/`PathFollow3D` para colocar objetos em caminhos.

```gdscript
# Percorrer caminho em velocidade constante:
var t = 0.0
func _process(delta):
    t += delta
    position = curve.sample_baked(t * curve.get_baked_length(), true)
```

### 19.6 Números Aleatórios

**Godot 4**: seed é inicializado automaticamente ao iniciar o projeto — não é necessário chamar `randomize()` no `_ready()`.

```gdscript
seed(12345)                     # seed fixo para resultados determinísticos
seed("Hello world".hash())      # string como seed
```

**Funções globais:**
```gdscript
randi() % N                     # int aleatório 0..N-1
randi_range(-10, 10)            # int aleatório no intervalo
randf()                         # float 0.0..1.0
randf_range(-4.0, 6.5)          # float no intervalo
randfn(mean, deviation)         # distribuição normal
array.pick_random()             # elemento aleatório de array (built-in)
```

**Probabilidade ponderada:**
```gdscript
func get_rarity() -> String:
    var r = randf()
    if r < 0.80: return "Common"    # 80%
    elif r < 0.95: return "Uncommon" # 15%
    else: return "Rare"              # 5%

# Alternativa com RandomNumberGenerator:
var rng = RandomNumberGenerator.new()
var weights = [0.5, 1.0, 1.0, 2.0]
var idx = rng.rand_weighted(weights)   # índice ponderado
```

**Shuffle bag** — distribuição mais uniforme sem repetição excessiva:
```gdscript
var _bag := []
var _bag_full := ["A", "B", "C", "D"]

func _ready():
    _bag = _bag_full.duplicate()
    _bag.shuffle()

func pick() -> String:
    if _bag.is_empty():
        _bag = _bag_full.duplicate()
        _bag.shuffle()
    return _bag.pop_front()
```

**Ruído procedural (`FastNoiseLite`)** — valores que mudam suavemente (terrain, texturas):
```gdscript
var _noise = FastNoiseLite.new()

func _ready():
    _noise.noise_type = FastNoiseLite.TYPE_SIMPLEX_SMOOTH
    _noise.seed = randi()
    _noise.fractal_octaves = 4
    _noise.frequency = 1.0 / 20.0
    print(_noise.get_noise_1d(0))    # float -1.0..1.0
    print(_noise.get_noise_2d(x, y)) # ruído 2D
```

**CSPRNG (`Crypto`)** — para criptografia, autenticação (não gameplay — muito mais lento):
```gdscript
var crypto := Crypto.new()
var bytes := crypto.generate_random_bytes(8)
var rand_int := bytes.decode_u32(0)   # uint32 do offset 0
```

- **Regra**: Use `randi_range()` / `randf_range()` em vez de `randi() % N + offset` para evitar viés de módulo.
- **Regra**: Use shuffle bag em vez de `pick_random()` quando a distribuição uniforme ao longo do tempo importa (loot tables, spawn de inimigos, trilhas musicais).

> ⚠ Evite: Usar `Crypto` para gameplay — use apenas para necessidades de segurança reais (tokens, chaves, hashes autenticados).

---

## 20 Performance

### 20.1 Princípios de Otimização

- **Medir antes de otimizar**: Use o profiler embutido (Debugger → Profiler) ou `Time.get_ticks_usec()` para isolar bottlenecks. Nunca otimize às cegas.
- **Bottleneck math**: Otimizar uma função que consome 9% do frame traz ganho mínimo; foque no que consome mais.
- **CPU vs GPU**: O frame time é determinado pelo mais lento dos dois. Reduzir o tempo de CPU não ajuda se o gargalo está na GPU.

```gdscript
var t = Time.get_ticks_usec()
update_enemies()
print("update_enemies: %d µs" % (Time.get_ticks_usec() - t))
```

- **Regra**: Profile primeiro, depois otimize — premature optimization é contraproducente.
- **Regra**: Prefira design performático (algoritmos e estruturas de dados corretos) a micro-otimizações de código.

### 20.2 Otimização de CPU

**Linguagens** (ordem crescente de performance, decrescente de facilidade):
`GDScript` → `C#` → `C++/GDExtension`

Use GDScript para lógica de jogo. Mova cálculos pesados (IA, geração procedural) para C# ou GDExtension se necessário.

**SceneTree overhead**: Cada node tem custo em `_process` / `_physics_process`. Para grandes quantidades de entidades, considere:
- Remover nodes da árvore com `remove_child()` em vez de `hide()` / `set_process(false)`.
- Usar Server APIs diretamente (ver 20.4) — zero overhead de node.

**Física**: Reduza a taxa de tick física (Project Settings → Physics → Common → Physics Ticks per Second) para cenas não-realtime. Ative physics interpolation para compensar jitter visual.

**Caches de CPU**: Prefira acesso linear a arrays a jumping aleatório em memória — dados contíguos maximizam cache hits.

### 20.3 Otimização de GPU

**Draw calls / batching**:
- 2D: batching automático agrupa sprites com mesma textura/material em uma única draw call.
- 3D: combine meshes estáticas antecipadamente (editor ou código). Meshes joinadas não podem ser culled individualmente — equilibre merge com culling.

**Materials / Shaders**:
- Reutilize o mesmo material entre objetos; quanto menos materiais distintos, mais rápido o rendering.
- Use `StandardMaterial3D` — o engine reutiliza shaders automaticamente entre instâncias com mesma configuração.

**Fill rate**:
- Shaders complexos e texturas grandes aumentam o custo por pixel. Simplifique shaders em mobile.
- Transparência é cara: cada pixel transparente obriga render em painter's order e impede uso do Z-buffer. Minimize áreas transparentes.
- Sombras: reduza o tamanho de shadowmaps; desative sombras em luzes pequenas/distantes.

**Mobile (tile-based renderers)**:
- Evite concentração de vértices em pequena área da tela (sobrecarrega uma tile).
- Overdraw (pixel renderizado mais de uma vez) é penalizado em mobile — use geometria mais simples e LOD.
- Teste o jogo em hardware mobile cedo no desenvolvimento.

> ⚠ Evite: Chamar funções que retornam dados do `RenderingServer` / `PhysicsServer` a cada frame — essas chamadas são síncronas e travam o servidor até completar.

### 20.4 Optimization using Servers (Low-level API)

Godot expõe servers de baixo nível (`RenderingServer`, `PhysicsServer2D/3D`, `AudioServer`) que podem ser usados diretamente, sem nodes na SceneTree, para máxima performance em cenários com dezenas de milhares de objetos.

**RIDs**: Handles opacos retornados pelos servers. Todos os objetos criados via server API são identificados por RIDs.

```gdscript
# Criar sprite via RenderingServer (sem node)
var ci = RenderingServer.canvas_item_create()
RenderingServer.canvas_item_set_parent(ci, get_canvas_item())
var tex = load("res://player.png")
RenderingServer.canvas_item_add_texture_rect(ci, Rect2(-tex.get_size()/2, tex.get_size()), tex)
RenderingServer.canvas_item_reset_physics_interpolation(ci)  # necessário no primeiro frame

# Mover
RenderingServer.canvas_item_set_transform(ci, Transform2D().translated(Vector2(x, y)))

# Limpar primitivos (devem ser re-adicionados para redesenhar)
RenderingServer.canvas_item_clear(ci)
```

```gdscript
# Criar RigidBody2D via PhysicsServer (sem node)
var body = PhysicsServer2D.body_create()
PhysicsServer2D.body_set_mode(body, PhysicsServer2D.BODY_MODE_RIGID)
var shape = PhysicsServer2D.rectangle_shape_create()
PhysicsServer2D.shape_set_data(shape, Vector2(10, 10))
PhysicsServer2D.body_add_shape(body, shape)
PhysicsServer2D.body_set_space(body, get_world_2d().space)
PhysicsServer2D.body_set_force_integration_callback(body, self, "_body_moved", 0)
```

- **Regra**: Ao usar Server API, chame `canvas_item_reset_physics_interpolation()` no primeiro frame para evitar teleporte visual.
- **Regra**: Mantenha referência à `Resource` (textura, mesh) fora do server — caso contrário o RID é invalidado quando o resource é coletado.

### 20.5 Threads

Godot suporta multithreading via `Thread`, `Mutex` e `Semaphore`.

**Thread básica:**
```gdscript
var thread: Thread

func _ready():
    thread = Thread.new()
    thread.start(_worker.bind("dados"))

func _worker(userdata):
    # roda em thread separada
    pass

func _exit_tree():
    thread.wait_to_finish()  # obrigatório — libera recursos da thread
```

**Mutex** (proteger dados compartilhados):
```gdscript
var mutex := Mutex.new()
var counter := 0

func _increment():
    mutex.lock()
    counter += 1
    mutex.unlock()
```

**Semaphore** (thread "on demand"):
```gdscript
var sem := Semaphore.new()

func _ready():
    thread.start(_worker)

func _worker():
    while true:
        sem.wait()        # suspende até post()
        # processar trabalho

func trigger_work():
    sem.post()            # acorda a thread
```

**Regras de thread-safety:**
- `SceneTree` **não é** thread-safe. Use `call_deferred()` / `set_deferred()` para modificar nodes a partir de threads.
- Construir sub-árvores de nodes fora da SceneTree é seguro; adicione à árvore via `add_child.call_deferred(node)`.
- `NavigationServer` é thread-safe. `RenderingServer` e `PhysicsServer` requerem "Thread Model: Separate" nas Project Settings.
- Arrays/Dictionaries GDScript: leitura/escrita de elementos é segura entre threads; resize/add/remove requer Mutex.
- Carregue resources em uma única thread — carregar o mesmo resource em múltiplas threads simultâneas causa corrupção.

> ⚠ Evite: Criar threads just-in-time dentro de `_process()` — criação de thread é lenta. Crie threads antecipadamente (ex: durante loading).

### 20.6 Occlusion Culling

Godot usa **Embree** (CPU) para occlusion culling — rasteriza um buffer de baixa resolução em paralelo para descartar objetos ocultos antes de enviá-los à GPU.
- Adicione `OccluderInstance3D` nodes com `Occluder3D` resources (Box, Sphere, Quad, Mesh, Polyhedral).
- Clique "Bake Occluders" no editor para gerar occluders simplificados automaticamente.
- Vantagens sobre portals/GPU culling: sem setup manual, sem frame delay, comportamento consistente em todos os drivers/renderers.

**Regra**: use shapes simples (Quad, Box) para occluders dinâmicos — mover occluders com mesh complexa em runtime é lento. Prefira bake de occluders simplificados para geometria estática.

### 20.7 LOD (Level of Detail)

**Automatic Mesh LOD:**
- LODs gerados automaticamente na importação via **meshoptimizer** (sem configuração manual).
- O engine seleciona LOD por `screen coverage` (cobertura de tela); cada Viewport pode usar LOD diferente (correto em split-screen).
- Shadow meshes (vértices soldados, sem smoothing) são geradas junto com os LODs — reduz vertex throughput em shadow rendering.
- Ajuste o multiplicador em Project Settings > Rendering > Mesh LOD > Threshold Scale.

**Visibility Range (HLOD manual):**
- Em qualquer `Node3D`, configure `Visibility Range Begin/End` para controlar distâncias mínima/máxima de exibição.
- Use `visibility_range_begin_margin` / `visibility_range_end_margin` para fade suave entre LODs.
- Combine com `GeometryInstance3D.visibility_range_fade_mode` para blending visual.

**Regra**: LOD automático cobre a maioria dos casos — use Visibility Range apenas para HLOD explícito (ex.: substituir mesh 3D por impostora ou Sprite3D à distância).

---

## 21 Networking

### 21.1 High-level Multiplayer (ENet / RPC)

Godot usa `MultiplayerAPI` + `ENetMultiplayerPeer` para multiplayer P2P e cliente-servidor. Gerenciado pelo `SceneTree`.

**Inicializar conexão:**
```gdscript
# Servidor
var peer = ENetMultiplayerPeer.new()
peer.create_server(PORT, MAX_CLIENTS)
multiplayer.multiplayer_peer = peer

# Cliente
var peer = ENetMultiplayerPeer.new()
peer.create_client(IP_ADDRESS, PORT)
multiplayer.multiplayer_peer = peer

# Encerrar conexão
multiplayer.multiplayer_peer = OfflineMultiplayerPeer.new()
```

**Signals de conexão:**
```gdscript
multiplayer.peer_connected.connect(_on_peer_connected)      # novo peer conectou
multiplayer.peer_disconnected.connect(_on_peer_disconnected)
multiplayer.connected_to_server.connect(_on_connected_ok)   # apenas no cliente
multiplayer.connection_failed.connect(_on_failed)
multiplayer.server_disconnected.connect(_on_server_disc)
```

- Server ID é sempre `1`. `multiplayer.get_unique_id()` retorna ID do peer local.
- `multiplayer.is_server()` verifica se é o servidor.

**RPCs (`@rpc`):**
```gdscript
# Chamar em todos os peers
@rpc("authority", "call_remote", "reliable", 0)
func my_rpc(data):
    pass

func _ready():
    if multiplayer.is_server():
        my_rpc.rpc()            # chama em todos os clientes
        my_rpc.rpc_id(2, data)  # chama só no peer 2
```

Parâmetros do `@rpc`:
| Parâmetro | Opções |
|---|---|
| mode | `"authority"` (só servidor chama) · `"any_peer"` (clientes também podem chamar) |
| sync | `"call_remote"` (não chama localmente) · `"call_local"` (chama também no sender) |
| transfer_mode | `"reliable"` · `"unreliable"` · `"unreliable_ordered"` |
| channel | índice inteiro (padrão 0) |

```gdscript
# Input do cliente → servidor
@rpc("any_peer", "call_local", "reliable")
func send_input(action: String):
    var sender = multiplayer.get_remote_sender_id()
    # processar input do sender
```

- **Regra**: A assinatura `@rpc` (modo, sync, transfer) deve ser idêntica em cliente e servidor — o engine valida com checksum.
- **Regra**: Para nodes criados com `add_child()` que usam RPCs, passe `force_readable_name = true` para garantir NodePath consistente entre peers.

**Lobby pattern (Autoload):**
```gdscript
# Autoload "Lobby" — registrar info do player no join
func _on_player_connected(id):
    _register_player.rpc_id(id, player_info)

@rpc("any_peer", "reliable")
func _register_player(info):
    var sender_id = multiplayer.get_remote_sender_id()
    players[sender_id] = info

# Carregar scene em todos os peers
@rpc("call_local", "reliable")
func load_game(path: String):
    get_tree().change_scene_to_file(path)
```

> ⚠ Evite: Lógica de negócio crítica apenas no cliente — sempre valide no servidor. Networking expõe a aplicação a exploits se mal implementado.

### 21.2 HTTP Requests

`HTTPRequest` (node) é a forma mais simples de fazer requisições HTTP em Godot.

```gdscript
func _ready():
    $HTTPRequest.request_completed.connect(_on_done)
    $HTTPRequest.request("https://api.example.com/data")

func _on_done(result, code, headers, body):
    var json = JSON.parse_string(body.get_string_from_utf8())
    print(json)
```

**POST com JSON:**
```gdscript
var payload = JSON.stringify({"key": "value"})
$HTTPRequest.request(url, ["Content-Type: application/json"],
                     HTTPClient.METHOD_POST, payload)
```

**Headers customizados:**
```gdscript
$HTTPRequest.request(url, ["Authorization: Bearer TOKEN"])
```

- **Regra**: Um `HTTPRequest` node suporta apenas uma requisição simultânea. Crie/destrua nodes dinamicamente se precisar de múltiplas requisições em paralelo.
- **Regra**: No export Android, habilite a permissão INTERNET no export preset, senão toda comunicação de rede é bloqueada pelo OS.

> ⚠ Evite: Embutir credenciais (tokens, senhas, chaves de API) no código do jogo — o executável pode ser decompilado e os dados extraídos.

---

## 22. Export

### 22.1 Workflow de Export

**Passos obrigatórios:**
1. Instalar export templates: Editor → Editor menu → **Install Export Templates** (arquivo `.tpz` baixado do site oficial).
2. Abrir **Project → Export** → clicar em **Add…** → escolher plataforma alvo.
3. Configurar o preset (a maioria das opções padrão é suficiente).
4. Clicar em um dos botões de export:

| Botão | Resultado |
|---|---|
| **Export All** | Executa todos os presets com `Export Path` definido |
| **Export Project** | Exporta o preset selecionado como binário + dados do projeto |
| **Export PCK/ZIP** | Exporta apenas os recursos do projeto, sem executável |

**Modos de seleção de recursos:**

| Modo | Comportamento |
|---|---|
| Export all resources | Inclui tudo no projeto |
| Export selected scenes | Lista cenas; selecione manualmente |
| Export selected resources | Lista recursos; selecione manualmente |
| All except checked | Tudo, exceto os itens marcados na lista |
| Export as dedicated server | Remove todos os visuais (Mesh, Texture, Material…) e substitui por placeholders |

- **Regra**: Arquivos e pastas cujo nome começa com `.` (ponto) nunca são incluídos no PCK exportado — isso evita que `.git/` seja empacotado.
- Use os filtros de inclusão/exclusão no export preset para adicionar arquivos não-resource (`.txt`, `.json`, `.csv`) ou excluir tipos específicos (`.png`).

### 22.2 Arquivos de Configuração

| Arquivo | Conteúdo | VCS |
|---|---|---|
| `export_presets.cfg` | Configuração principal do export (plataformas, opções, modos) | Pode commitar com segurança |
| `.godot/export_credentials.cfg` | Senhas, chaves de criptografia, credenciais de plataforma | **Nunca commitar** |

- **Regra**: Ao clonar o projeto em uma máquina nova, copie manualmente `export_credentials.cfg` da máquina anterior — ele não está no VCS.

### 22.3 Export pela Linha de Comando

```bash
# Export de release (binário + dados)
godot --export-release "Windows Desktop" build/game.exe

# Export de debug
godot --export-debug "Windows Desktop" build/game.exe

# Exportar apenas o PCK (sem executável)
godot --export-pack "Windows Desktop" build/game.pck

# Combinar com --path para não precisar de cd
godot --path /caminho/para/projeto --export-release "Windows Desktop" build/game.exe
```

- O nome do preset deve corresponder exatamente ao configurado no editor (use aspas se houver espaços).
- O caminho de saída é relativo ao diretório do projeto ou absoluto — **não** relativo ao diretório atual do terminal.
- Extensões esperadas por plataforma: Windows `.exe`, macOS `.app`/`.zip`, Linux `.x86_64`, HTML5 `.zip`, Android `.apk`, iOS `.zip`.

### 22.4 PCK vs ZIP

| Formato | Compressão | Velocidade | Ferramentas do OS |
|---|---|---|---|
| **PCK** (padrão) | Nenhuma | Mais rápido | Não nativo (ferramentas de terceiros) |
| **ZIP** | Sim | Mais lento | Nativo (ideal para mods pelo usuário) |

- **Regra**: Use PCK para distribuição padrão; use ZIP quando precisar que usuários possam inspecionar ou criar arquivos de mod com ferramentas comuns.

> ⚠ Evite (bug conhecido): ao usar ZIP como pack principal, o binário não o carrega automaticamente — crie um launcher script:
> ```bat
> :: launch.bat (Windows)
> @echo off
> my_project.exe --main-pack my_project.zip
> ```
> ```bash
> # launch.sh (Linux) — dar chmod +x ao arquivo
> ./my_project.x86_64 --main-pack my_project.zip
> ```

### 22.5 DLC, Patches e Mods (Resource Packs em Runtime)

Godot permite carregar PCK/ZIP adicionais em tempo de execução para DLC, patches ou suporte a mods.

```gdscript
func _your_function():
    var success = ProjectSettings.load_resource_pack(
        OS.get_executable_path().get_base_dir().path_join("mod.pck")
    )
    if success:
        var imported_scene = load("res://mod_scene.tscn")
```

- Arquivo com o **mesmo caminho** de um recurso já carregado **substitui** o original — use isso para patches; passe `false` como segundo argumento para desativar esse comportamento.
- **Regra**: Carregue resource packs o mais cedo possível. Coloque `ProjectSettings.load_resource_pack()` no `_init()` de um Autoload — não em `_ready()` — para evitar que cenas já carregadas por `preload()` ignorem o pack.

```gdscript
# Autoload: load_mods.gd
func _init():
    ProjectSettings.load_resource_pack(
        OS.get_executable_path().get_base_dir().path_join("mod.pck")
    )
```

> ⚠ Evite: Carregar o resource pack no `_ready()` de uma scene de menu — se a scene usou `preload()` para outras scenes, elas já foram carregadas antes do pack e não serão substituídas.

---

## 23. Navigation

### 23.1 Visão Geral — Objetos de Navegação

Godot oferece duas famílias de navegação para 2D/3D:

| Classe | Quando usar |
|---|---|
| `AStar2D` / `AStarGrid2D` | Gameplay cell-based (grade), posições discretas pré-definidas |
| `NavigationServer2D/3D` | Realtime — qualquer posição dentro de um NavMesh; escala bem em mundos grandes |

**RID types do NavigationServer:**

| RID | Representa |
|---|---|
| `NavMap` | Mapa de navegação; contém regions e agents; sincroniza a cada physics frame |
| `NavRegion` | Região com dados de NavMesh; pode ser habilitada/desabilitada; filtrada por layer |
| `NavLink` | Conecta dois pontos de NavMesh sobre distâncias arbitrárias |
| `NavAgent` | Agente de avoidance (círculo 2D / esfera 3D) |
| `NavObstacle` | Obstáculo que limita velocidade dos agentes no avoidance |

**Nodes helpers (scene tree):**

| Node | Função |
|---|---|
| `NavigationRegion2D/3D` | Mantém `NavigationPolygon` / `NavigationMesh`; contribui ao mapa |
| `NavigationAgent2D/3D` | Helper de pathfinding + pathfollowing + avoidance para o node pai |
| `NavigationObstacle2D/3D` | Obstáculo estático/dinâmico para baking de mesh e/ou avoidance |
| `NavigationLink2D/3D` | Atalho entre dois pontos do NavMesh (ex.: teleporte, escada) |

### 23.2 Setup Mínimo (2D)

```gdscript
# No CharacterBody2D com NavigationAgent2D filho
extends CharacterBody2D

var movement_speed := 200.0
@onready var nav_agent: NavigationAgent2D = $NavigationAgent2D

func _ready():
    nav_agent.path_desired_distance = 4.0
    nav_agent.target_desired_distance = 4.0
    actor_setup.call_deferred()   # não await em _ready direto

func actor_setup():
    await get_tree().physics_frame  # espera NavigationServer sincronizar
    nav_agent.target_position = Vector2(300, 200)

func _physics_process(_delta):
    if nav_agent.is_navigation_finished():
        return
    var next := nav_agent.get_next_path_position()
    velocity = global_position.direction_to(next) * movement_speed
    move_and_slide()
```

- **Regra**: Sempre use `call_deferred()` + `await get_tree().physics_frame` antes de fazer a primeira query de path — o mapa ainda está vazio em `_ready()`.
- Deixe margem suficiente entre o polígono de navegação e os colliders para evitar que o personagem fique preso.

### 23.3 NavigationServer — Sincronização e Threading

- O NavigationServer **não aplica mudanças imediatamente** — aguarda o meio do physics frame para sincronizar tudo junto.
- Toda chamada que altera estado (setters, deletes) requer sincronização antes de produzir efeito.
- `get_*()` que não alteram estado podem ser chamados a qualquer momento, mas não refletem mudanças do mesmo frame.
- O server é **thread-safe**: enfileira mudanças para o momento de sync; pode receber chamadas de threads secundárias.

**Query procedural de path (sem nodes):**

```gdscript
func custom_setup():
    var map: RID = NavigationServer3D.map_create()
    NavigationServer3D.map_set_up(map, Vector3.UP)
    NavigationServer3D.map_set_active(map, true)

    var region: RID = NavigationServer3D.region_create()
    NavigationServer3D.region_set_transform(region, Transform3D())
    NavigationServer3D.region_set_map(region, map)

    var nav_mesh := NavigationMesh.new()
    nav_mesh.set_vertices(PackedVector3Array([
        Vector3(0, 0, 0), Vector3(9, 0, 0), Vector3(0, 0, 9)
    ]))
    nav_mesh.add_polygon(PackedInt32Array([0, 1, 2]))
    NavigationServer3D.region_set_navigation_mesh(region, nav_mesh)

    await get_tree().physics_frame   # espera sync

    var path = NavigationServer3D.map_get_path(map, Vector3(0.1,0,0.1), Vector3(1,0,1), true)
    print(path)
```

### 23.4 NavigationPaths

Obtenha paths diretamente do server sem nodes extras, desde que o mapa já tenha NavMesh.

```gdscript
# 2D — mapa padrão do mundo
func get_path_2d(from: Vector2, to: Vector2) -> PackedVector2Array:
    var map := get_world_2d().get_navigation_map()
    return NavigationServer2D.map_get_path(map, from, to, true)

# 3D
func get_path_3d(from: Vector3, to: Vector3) -> PackedVector3Array:
    var map := get_world_3d().get_navigation_map()
    return NavigationServer3D.map_get_path(map, from, to, true)
```

Parâmetro `optimize`:

| `optimize` | Resultado |
|---|---|
| `true` | Funnel algorithm — hugs corners; ideal para NavMesh com polígonos irregulares |
| `false` | Centro de cada aresta — ideal para grids uniformes |

### 23.5 NavigationAgent — Pathfinding, Following e Avoidance

**Pathfinding:** o path é atualizado quando `target_position` muda, o mapa muda ou o agente se desvia demais do path ideal (`path_max_distance`).

**Pathfollowing — propriedades chave:**

| Propriedade | Efeito |
|---|---|
| `path_desired_distance` | Avança índice interno quando chega a esta distância do próximo ponto |
| `target_desired_distance` | Considera target atingido quando chega a esta distância |
| `path_max_distance` | Força nova query se agente ficar tão longe do path ideal |

- `get_next_path_position()` deve ser chamado todo `_physics_process` até `is_navigation_finished()` → `true`.
- **Nunca** chame após o path terminar — causa jitter por continuar atualizando.

**Problemas comuns de pathfollowing:**

- *Path vazio no início*: query antes do sync → use deferred + `await physics_frame`.
- *Agente dançando entre dois pontos*: path resetado todo frame; não atualize `target_position` toda frame — só quando o alvo se mover o suficiente.
- *Backtracking*: agente rápido passa o `path_desired_distance` sem avançar o índice → aumente `path_desired_distance`.

**Avoidance (RVO):**

```gdscript
# Ativar avoidance
nav_agent.avoidance_enabled = true
nav_agent.velocity_computed.connect(_on_safe_velocity)

func _physics_process(_delta):
    var desired_vel = global_position.direction_to(nav_agent.get_next_path_position()) * speed
    nav_agent.velocity = desired_vel  # alimenta o agente; resultado chega via signal

func _on_safe_velocity(safe_vel: Vector2):
    velocity = safe_vel
    move_and_slide()
```

- Avoidance opera em espaço próprio — **não sabe** de NavMesh nem colisões físicas.
- `radius` = tamanho do agente; `neighbor_distance` = alcance de busca; `time_horizon_agents/obstacles` = tempo de predição.
- `avoidance_layers` / `avoidance_mask`: bitmasks — agente só evita objetos cujo layer bate com sua mask.
- `avoidance_priority`: agentes com prioridade maior ignoram os de prioridade menor.
- **Regra**: Mantenha `time_horizon` o mais baixo possível — agentes reduzem velocidade para evitar colisão dentro desse horizonte.

> ⚠ Evite: Cenários clínicos de avoidance (agentes indo diretamente uns contra os outros com velocidades opostas perfeitas) — o RVO assume comportamento natural de desvio lateral e falha nesses casos extremos.

### 23.6 NavigationObstacles

Dual-purpose: afeta baking de NavMesh e/ou avoidance dinâmico.

| Propriedade | Efeito |
|---|---|
| `affect_navigation_mesh` | Obstáculo remove geometria de NavMesh durante o bake |
| `avoidance_enabled` | Obstáculo influencia velocidade de agentes com avoidance |
| `carve_navigation_mesh` | Ignora offset de `agent_radius` ao cortar o NavMesh (efeito "stencil") |

- Obstáculo **não adiciona** geometria ao bake — apenas remove (nullifica voxels).
- **Regra**: Se o obstáculo não é usado para avoidance, desative `avoidance_enabled` para economizar CPU.

```gdscript
# Obstáculo procedural durante bake
var outline = PackedVector2Array([Vector2(-50,-50), Vector2(50,-50),
                                   Vector2(50,50), Vector2(-50,50)])
var nav_mesh := NavigationPolygon.new()
var src_geo := NavigationMeshSourceGeometryData2D.new()
NavigationServer2D.parse_source_geometry_data(nav_mesh, src_geo, $RootNode)
src_geo.add_projected_obstruction(outline, true)  # true = carve
NavigationServer2D.bake_from_source_geometry_data(nav_mesh, src_geo)
```

### 23.7 NavigationLayers

Bitmask para filtrar regiões em queries de path — funciona como physics layers.

```gdscript
# Habilitar/desabilitar camada por índice (helper)
static func enable_layer(bitmask: int, idx: int) -> int:
    return bitmask | (1 << idx)

static func disable_layer(bitmask: int, idx: int) -> int:
    return bitmask & ~(1 << idx)

# Aplicar na region e no agente
region.navigation_layers = enable_layer(region.navigation_layers, 4)
agent.navigation_layers  = disable_layer(agent.navigation_layers, 4)

# Query com layer específica
var layers := enable_layer(0, 2)  # só layer 2
var path := NavigationServer2D.map_get_path(map, start, target, true, layers)
```

- Nodes também expõem `set_navigation_layer_value(n, bool)` / `get_navigation_layer_value(n)` para evitar operações bitwise manuais.

### 23.8 Debug de Navegação

- Visualização de NavMesh ativa por padrão no editor. Para ver em runtime: **Debug menu → Visible Navigation**.
- Ativar/desativar por script (apenas em debug builds):

```gdscript
NavigationServer2D.set_debug_enabled(true)
NavigationServer3D.set_debug_enabled(false)
```

- Configurações visuais: **ProjectSettings → debug/shapes/navigation** (cores, xray, faces aleatórias, edge connections).
- Monitor de performance: **Debugger → Monitors → Navigation Process** — tempo gasto pelo server no sync (NÃO inclui o pathfinding em si).

> ⚠ Evite: Usar funções de debug em código de release — elas só existem em builds de debug.

### 23.9 Otimização de Performance de Navegação

**Parsing de geometria (bake):**
- Prefira **formas de colisão física** como source geometry; meshes visuais têm de ser copiadas do GPU e são muito mais detalhadas que o necessário.
- Nunca use mesh visual detalhada diretamente — use uma versão LOD simplificada ou formas primitivas.

**Baking:**
- Sempre bake em **background thread** em runtime — mesmo NavMeshes pequenos podem levar mais de 1 frame.
- Aumente `cell_size` / `cell_height` ao máximo que não prejudique a qualidade de navegação.
- Use `SamplePartitionType` = `monotone` ou `layers` em geometria predominantemente plana — são muito mais rápidos que `watershed`.
- **Nunca escale source geometry com nodes** — a escala pode não estar refletida nos dados reais e gera voxel grid enorme.

**Queries de path (NavigationAgent):**
- Não redefina `target_position` todo frame — compare distância e só atualize quando o alvo se mover o suficiente.
- Não chame "is position reachable?" separado: já é o equivalente de uma query completa; faça a query e analise o último ponto do path retornado.
- Distribua os agentes em **grupos de atualização** ou use `Timer` aleatório para evitar que todos peçam novo path no mesmo frame.

**Path search:**
- Custo do A* correlaciona com quantidade de polígonos/arestas, não com tamanho do mundo.
- NavMeshes com poucos polígonos grandes são muito mais rápidos que grids com muitos polígonos pequenos.
- Target inalcançável é mais caro que atingível — o A* percorre todo o grafo antes de confirmar impossibilidade; otimize NavMeshes para minimizar esse overhead.

**Sincronização do mapa:**
- Prefira merge de NavMeshes por **vértice** (rápido) em vez de edge connection (custoso). Use o monitor de navegação para checar a proporção vertex-merged vs edge-connected.

**Regra**: Use o monitor **Navigation Process** no Debugger para identificar gargalos antes de otimizar.

---

## 24. TileMaps

TileMaps usam `TileMapLayer` (Godot 4.x) para pintar tiles em grade — mais rápido que Sprite2D individuais e otimizado para grandes mapas.

### 24.1 TileSet — Atlas e Configuração

**Fluxo básico:**
1. Crie um `TileMapLayer` node.
2. Crie um `TileSet` resource no Inspector — defina tile shape (Square, Isometric, Hexagon) e tile size.
3. Arraste a tilesheet para o painel **TileSet** → responda "Yes" para gerar tiles automaticamente (regiões transparentes são ignoradas).
4. Salve o TileSet como resource externo (`.tres`) para reutilizar em múltiplos `TileMapLayer`.

**Propriedades do atlas:**

| Propriedade | Descrição |
|---|---|
| Margins | Bordas da imagem que não são tiles (pixels) |
| Separation | Espaço entre tiles (guides/outlines) |
| Texture Region Size | Tamanho de cada tile no atlas |
| Use Texture Padding | Borda 1px para evitar texture bleeding (recomendado) |

- Para múltiplas tilesheets, crie atlases adicionais.
- Tiles de cenas: use **Scenes Collection** para colocar nodes complexos (partículas, AudioStreamPlayer2D) como tiles.

> ⚠ Evite: Scene tiles para sprites simples — use atlas. Scene tiles têm overhead maior pois cada tile instancia uma cena inteira.

**Mesclando atlases:**  
TileSet > menu "⋮" > *Open Atlas Merging Tool* → selecione atlases → *Merge*. Tile proxies são criados automaticamente para preservar TileMaps existentes.

### 24.2 Collision, Navigation e Occlusion no TileSet

Antes de definir formas, crie as camadas no Inspector do TileSet:
- **Physics Layers** → Add Element (para colisão)
- **Navigation Layers** → Add Element (para NavigationMesh)
- **Occlusion Layers** → Add Element (para sombras/partículas)

**Editando colisão por tile (TileSet editor, modo Select):**
- Pressione `F` para gerar retângulo padrão de colisão.
- Remova um vértice clicando com botão direito → forma triangular.
- Arraste linha entre dois pontos para adicionar vértice.

**Propriedade painting** (múltiplos tiles ao mesmo tempo):
- Configure a forma no editor → clique/arraste para "pintar" a propriedade em vários tiles de uma vez.
- Útil para aplicar collision shapes idênticas a dezenas de tiles rapidamente.

### 24.3 Terrain Sets (Autotiling)

Terrains substituem autotiles do Godot 3. Qualquer tile de terrain pode ser pintado manualmente OU via modo automático.

**Modos de terrain set:**

| Modo | Equivalente Godot 3 | Descrição |
|---|---|---|
| Match Corners and Sides | 3×3 | Conecta por cantos e lados |
| Match Corners | 3×3 minimal | Somente cantos |
| Match Sides | 2×2 | Somente lados |

**Setup:**
1. Inspector do TileSet → crie terrain set → crie terrain(s) dentro dele.
2. No TileSet editor (modo Select), selecione um tile → atribua *Terrain Set* e *Terrain* (IDs começam em 0).
3. Configure **Terrain Peering Bits**: defina quais vizinhos ativam o tile. `-1` = espaço vazio.

> **Regra**: Peering bits `-1` no topo fazem o tile só aparecer quando há espaço acima — use para tiles de borda de plataforma.

### 24.4 TileMapLayer — Configuração e Layers

Use múltiplos `TileMapLayer` nodes para separar background de foreground.

**Propriedades principais:**

| Propriedade | Descrição |
|---|---|
| TileSet | Resource TileSet usado |
| Y Sort Origin | Offset vertical para Y-sorting (top-down) |
| Rendering Quadrant Size | Tamanho do lote de renderização (padrão: 16 tiles) |
| Collision Enabled | Liga/desliga colisão |
| Use Kinematic Bodies | Colisões instanciadas como KinematicBody |
| Navigation Enabled | Liga/desliga geração de NavigationRegion |

**Regra**: Para pathfinding de qualidade, desative a Navigation do TileMapLayer após o design e bake um `NavigationRegion2D` separado — a navigation built-in tem limitações de performance e qualidade.

### 24.5 Editor de TileMap — Modos de Pintura

Selecione o `TileMapLayer` e abra o painel **TileMap** na parte inferior do editor.

| Ferramenta | Atalho temporário | Descrição |
|---|---|---|
| Paint | — | Clique/arraste para colocar tiles; botão direito apaga |
| Line | Shift+drag | Linha de 1 tile de espessura |
| Rectangle | Ctrl+Shift+drag | Retângulo preenchido |
| Bucket Fill | — | Preenche área contígua (ou todo o mapa se Contiguous desligado) |
| Picker | Ctrl+click | Captura tile existente no mapa |
| Eraser | Botão direito | Combina com qualquer modo para apagar |
| Selection | — | Seleciona tiles colocados; Del remove; Ctrl+C/V copia/cola |

- Selecione múltiplos tiles no painel → eles são pintados como bloco.
- Rotate/flip enquanto pinta: use os botões na toolbar do TileMap editor (desde Godot 4.2).

### 24.6 Alternative Tiles, Patterns e Randomização

**Alternative tiles** — mesma imagem, configuração diferente (flipped, modulated, material distinto):
- Clique direito em tile base → *Create an Alternative Tile*.
- Propriedades relevantes: `Flip H`, `Flip V`, `Transpose` (rotações), `Modulate`, `Z Index`, `Y Sort Origin`.

**Randomização:**
- Habilite **Randomize** na toolbar → ao pintar, escolhe aleatoriamente entre tiles selecionados.
- **Scattering > 0**: probabilidade de não colocar nenhum tile — cria detalhes esparsos (grama, detritos).

**Patterns:**
- Modo Selection → selecione tiles → `Ctrl+C` → aba Patterns → `Ctrl+V` para salvar.
- Padrões são armazenados no TileSet (reutilizáveis em diferentes `TileMapLayer`).
- Use com Line/Rectangle/Fill para repetir o padrão na área pintada.

**Terrain — modos de pintura:**
- **Connect**: conecta automaticamente ao que já está no mapa.
- **Path**: conecta apenas tiles pintados no mesmo stroke — permite estradas adjacentes sem se unirem.

**Custom Data Layers:**
```gdscript
# Acessar metadata de um tile em runtime:
var tile_data = tile_map_layer.get_cell_tile_data(Vector2i(x, y))
if tile_data:
    var dmg = tile_data.get_custom_data("damage_per_second")  # nome definido no TileSet
```

---

## 25. Export por Plataforma

Esta seção complementa a seção 22 (workflow geral de export) com os requisitos específicos de cada plataforma.

### 25.1 Windows

**Arquiteturas disponíveis:** `x86_64` (padrão), `x86_32` (legacy 32-bit), `arm64` (Snapdragon X Elite).

**Code signing:**
- Requer **Windows SDK** (`SignTool.exe`) no Windows ou **osslsigncode** em Linux/macOS.
- Configure em *Editor Settings > Export > Windows > Sign Tool*.
- No export preset (Windows Desktop), habilite *Code Signing > Enabled* e aponte o certificado.

**PCK embedding:** suportado até ~3.89 GB total (executável + PCK).

**Ícone:** Godot converte automaticamente o project icon para `.ico`. Para controle fino de resolução, crie o `.ico` manualmente.

### 25.2 Linux

**Arquiteturas:** `x86_64`, `x86_32`, `arm64`, `arm32`, `rv64`, `ppc64`, `loongarch64`.

**Regra**: Não use o Android/Linux SDK do repositório da distro — costuma estar desatualizado. Instale o SDK oficial.

- Distribuição padrão: `x86_64`. Para Raspberry Pi 5 → `arm64`.
- `arm32` e demais arquiteturas são muito nichadas; exporte sob demanda.

### 25.3 macOS

**Formato:** Exportado como bundle `.app` Universal 2 (Intel x86_64 + Apple Silicon arm64).

> ⚠ Evite: Exportar `.app` a partir do Windows — o executável perde a flag de execução. Use `.zip` nesses casos, ou adicione a permissão via `chmod +x` em Linux/macOS.

**Code signing e notarização:**

| Cenário | Ferramenta | Ação |
|---|---|---|
| Apple Developer ID + macOS | Xcode codesign + altool | Assinar com identidade + notarizar via altool |
| Apple Developer ID + Linux/Win | PyOxidizer rcodesign | Assinar com PKCS#12 + notarizar via API |
| Sem certificado | Built-in ad-hoc | Assinatura ad-hoc — Gatekeeper bloqueia downloads externos |

Após notarização, sempre execute `staple` para incluir o ticket no bundle:
```bash
xcrun stapler staple exported_app.app
# ou com rcodesign:
rcodesign staple exported_app.app
```

**Bundle identifier** é obrigatório — defina em *Export > Application > Bundle Identifier*.

### 25.4 Android

**Pré-requisitos:**
1. **OpenJDK 17** (versões mais novas também suportadas).
2. **Android SDK** com pacotes:
   - `platform-tools`, `build-tools;35.0.1`, `platforms;android-35`
   - `cmdline-tools;latest`, `cmake;3.10.2.4988404`, `ndk;28.1.13356709`

```bash
sdkmanager --sdk_root=<path> "platform-tools" "build-tools;35.0.1" \
  "platforms;android-35" "cmdline-tools;latest" \
  "cmake;3.10.2.4988404" "ndk;28.1.13356709"
```

3. Configure em *Editor Settings > Android*: `Java SDK Path` e `Android SDK Path`.

**Ícones:**
- **Main Icon**: mínimo 192×192 px (Android ≤ 7).
- **Adaptive Icon** (foreground + background): mínimo 432×432 px (Android 8+). Zona segura: círculo central de 264 px.
- **Themed Icon** (monochrome): mínimo 432×432 px (Android 13+, opcional).

> ⚠ Evite: Reaproveitar o project icon sem criar ícones adaptativos — em Android 8+ o ícone pode ser cortado pelo launcher.

**C# no Android**: suportado desde Godot 4.2, mas ainda experimental.

### 25.5 iOS

**Requisitos:**
- macOS com Xcode instalado (export para iOS **exige** macOS).
- Export templates instalados (*Editor > Manage Export Templates*).
- **App Store Team ID** (10 caracteres, ex.: `ABCDE12XYZ`) e **Bundle Identifier** são obrigatórios.

**Fluxo:**
1. *Project > Export* → Add → iOS.
2. Preencha Team ID e Bundle Identifier.
3. *Export Project* → escolha pasta (vazia) e nome do projeto Xcode.
4. Abra no Xcode → build/deploy/App Store normalmente.

> ⚠ Evite: Espaços no nome do projeto exportado — corrompe o arquivo `.xcodeproj`.

**C# no iOS**: suportado desde Godot 4.2, experimental.

### 25.6 Web (HTML5)

**Requisitos:** WebAssembly + WebGL 2.0. Rendering method: apenas **Compatibility** (Forward+/Mobile não suportados na Web).

**Single-thread vs Multi-thread:**

| Modo | Prós | Contras |
|---|---|---|
| Single-thread (padrão desde 4.3) | Compatível com itch.io, Poki, CrazyGames; funciona em macOS/iOS | Sem threads, menor performance |
| Multi-thread | Melhor performance | Exige `SharedArrayBuffer` + cabeçalhos COOP/COEP; sem ads/integrations |

**Regra**: Use single-thread por padrão. Multi-thread só se o jogo exigir performance extrema e você controlar o servidor.

**Nome do arquivo:** exporte como `index.html` para que servidores web o sirvam como padrão.

**Áudio na Web (desde Godot 4.3):**
- Padrão: **Sample** (Web Audio API) — baixa latência, sem AudioEffects.
- Para AudioEffects/reverb: mude *Audio > General > Default Playback Type.web* para `Stream` (maior latência).

**Limitações:**
- C# não suportado na Web em Godot 4 (use Godot 3 para C# + Web).
- WebGL 2.0 tem problemas em Safari — prefira Chromium ou Firefox.
- Use feature tags para aplicar configurações de baixo desempenho em mobile Web.

**Servindo arquivos:** arquivos exportados devem ser servidos com os cabeçalhos corretos (especialmente para multi-thread). Use `python -m http.server` ou equivalente para testes locais.

### 25.7 Servidor Dedicado (Headless)

**Modo headless** — executa Godot sem GPU/display:
```bash
./godot --headless          # qualquer plataforma, qualquer build
./godot --headless meu.pck  # carrega PCK em headless
```

**Export template vs Editor:**
- Use **export template** (debug ou release) para servidores de produção — menor, sem funcionalidades do editor.
- Editor binary funciona em headless mas não é recomendado para produção.

**Reduzindo tamanho do PCK do servidor:**
1. Crie um export preset dedicado para o servidor.
2. Na aba *Resources* do preset → selecione *Export as dedicated server*.
3. Godot remove texturas e materiais automaticamente, preservando referências.
4. A feature tag `dedicated_server` é adicionada automaticamente → use `OS.has_feature("dedicated_server")` para bifurcar lógica cliente/servidor.

```gdscript
func _ready() -> void:
    if OS.has_feature("dedicated_server"):
        # inicia lógica de servidor
        _start_server()
    else:
        # inicia lógica de cliente
        _start_client()
```

> ⚠ Evite: Exportar o mesmo PCK do cliente para o servidor — inclui texturas desnecessárias que aumentam muito o tamanho do download.

---

## 26. File e Data I/O

### 26.1 Caminhos de Arquivo (res:// e user://)

Godot usa separadores de caminho no estilo UNIX (`/`) em todas as plataformas.

| Prefixo | Descrição | Escrita em builds? |
|---|---|---|
| `res://` | Raiz do projeto (relativo ao `project.godot`) | Não — somente leitura em exports |
| `user://` | Dados persistentes do usuário, criado automaticamente | Sim — sempre gravável |

**Localização de `user://` no disco:**

| Plataforma | Caminho (padrão) |
|---|---|
| Windows | `%APPDATA%\Godot\app_userdata\<projeto>` |
| macOS | `~/Library/ApplicationSupport/Godot/app_userdata/<projeto>` |
| Linux | `~/.local/share/godot/app_userdata/<projeto>` |

Para usar pasta própria (ex.: `MinhaEmpresa/MeuJogo`), habilite `application/config/use_custom_user_dir` + defina `application/config/custom_user_dir_name` nas Project Settings.

**Métodos úteis de String para caminhos:**
```gdscript
path.get_base_dir()        # diretório pai
path.get_file()            # nome do arquivo com extensão
path.get_extension()       # extensão sem ponto
path.get_basename()        # caminho sem extensão
path.path_join("sub/f")    # concatena de forma segura
path.is_absolute_path()
```

**Converter entre res:// e path absoluto:**
```gdscript
var abs = ProjectSettings.globalize_path("res://data/config.cfg")
var rel = ProjectSettings.localize_path(abs)
```

> ⚠ Evite: Escrever em `res://` em runtime — em exports o filesystem é somente leitura. Use sempre `user://` para dados persistentes.

### 26.2 FileAccess — Leitura e Escrita

```gdscript
# Texto
func save_text(content: String) -> void:
    var file = FileAccess.open("user://data.txt", FileAccess.WRITE)
    file.store_string(content)

func load_text() -> String:
    var file = FileAccess.open("user://data.txt", FileAccess.READ)
    return file.get_as_text()

# Binário — bytes brutos
func save_binary(data: PackedByteArray) -> void:
    var file = FileAccess.open("user://data.bin", FileAccess.WRITE)
    file.store_buffer(data)

func load_binary() -> PackedByteArray:
    var file = FileAccess.open("user://data.bin", FileAccess.READ)
    return file.get_buffer(file.get_length())
```

**Verificar existência antes de abrir:**
```gdscript
if FileAccess.file_exists("user://savegame.save"):
    var file = FileAccess.open(...)
```

**Serialização binária com Variant** (alternativa ao JSON — suporta Vector2, Color, etc.):
```gdscript
# Salvar qualquer Variant:
var data = {"pos": Vector2(10, 20), "hp": 100}
var file = FileAccess.open("user://save.bin", FileAccess.WRITE)
file.store_var(data)

# Carregar:
var file = FileAccess.open("user://save.bin", FileAccess.READ)
var data = file.get_var()
```

**`var_to_bytes` / `bytes_to_var`** — serialização sem arquivo (rede, ZIP):
```gdscript
var bytes: PackedByteArray = var_to_bytes(my_variant)
var value = bytes_to_var(bytes)

# Com objetos completos (não apenas IDs):
var bytes = var_to_bytes_with_objects(my_dict)
var value = bytes_to_var_with_objects(bytes)
```

**JSON vs Binário:**

| Critério | JSON | Binário (`store_var`) |
|---|---|---|
| Legibilidade | Humano-legível, fácil de debugar | Não legível |
| Tamanho | Maior | Menor |
| Tipos suportados | Limitado (sem Vector2/Color/etc.) | Todos os tipos Variant |
| Encode/decode extra | Necessário para tipos customizados | Não necessário |

> 💡 Para configurações do usuário, prefira `ConfigFile` — tem API de seções/chaves e suporta todos os tipos Variant nativamente (ver seção 15.3).

### 26.3 Save Game — Referência Rápida

Padrão completo (grupo "Persist" + JSON) está documentado em **seção 15.3**. Resumo das escolhas de serialização:

- **JSON**: use para saves legíveis e debugáveis; exige conversão de Vector2/Color para componentes escalares.
- **`store_var` / `get_var`**: use para saves compactos; suporta todos os tipos Variant incluindo Arrays e Dicionários aninhados.
- **`PROPERTY_USAGE_STORAGE`**: apenas propriedades com essa flag são incluídas em `store_var` com full objects.

### 26.4 Carregamento em Background (ResourceLoader Threaded)

Para telas de loading ou carregamento assíncrono durante gameplay:

```gdscript
const ENEMY_PATH = "res://Enemy.tscn"

func _ready():
    # Enfileira o carregamento em thread de background:
    ResourceLoader.load_threaded_request(ENEMY_PATH)

func _on_button_pressed():
    # Recupera o recurso (bloqueia se ainda não terminou):
    var enemy_scene = ResourceLoader.load_threaded_get(ENEMY_PATH)
    add_child(enemy_scene.instantiate())
```

**Verificar progresso (para barra de loading):**
```gdscript
func _process(_delta):
    var progress = []
    var status = ResourceLoader.load_threaded_get_status(ENEMY_PATH, progress)
    match status:
        ResourceLoader.THREAD_LOAD_IN_PROGRESS:
            $ProgressBar.value = progress[0] * 100  # 0.0 a 1.0
        ResourceLoader.THREAD_LOAD_LOADED:
            var scene = ResourceLoader.load_threaded_get(ENEMY_PATH)
            # usar scene...
        ResourceLoader.THREAD_LOAD_FAILED:
            push_error("Falha ao carregar: " + ENEMY_PATH)
```

- Combine com o recurso já carregado via `ResourceLoader.load()` normal para recursos pequenos.
- Para trocar a cena principal com loading screen, use `get_tree().change_scene_to_file()` + thread de background.

### 26.5 Carregamento de Arquivos em Runtime

Útil para mods, UGC (user-generated content) e conteúdo externo ao PCK.

**Imagens:**
```gdscript
# Detecção automática por extensão:
var image = Image.load_from_file("/path/to/image.png")

# Específico por formato (PNG, JPG, WebP, SVG, TGA, EXR, KTX):
var buf: PackedByteArray = FileAccess.get_file_as_bytes(path)
var image = Image.new()
image.load_png_from_buffer(buf)

# Converter para textura exibível:
var texture = ImageTexture.create_from_image(image)
$Sprite2D.texture = texture
```

**Áudio/Vídeo:**
```gdscript
var stream = AudioStreamOggVorbis.load_from_file("user://music.ogg")
# ou:
var stream = AudioStreamMP3.new()
stream.data = FileAccess.get_file_as_bytes("user://music.mp3")
$AudioStreamPlayer.stream = stream
$AudioStreamPlayer.play()
```

**Cenas 3D (glTF em runtime):**
```gdscript
var gltf = GLTFDocument.new()
var state = GLTFState.new()
gltf.append_from_file("user://model.glb", state)
var scene = gltf.generate_scene(state)
add_child(scene)
```

**ZIP Archives:**
```gdscript
# Ler arquivos de um ZIP:
var reader = ZIPReader.new()
reader.open("user://pack.zip")
for file in reader.get_files():
    var bytes = reader.read_file(file)
    # processar bytes...

# Criar/escrever ZIP:
var packer = ZIPPacker.new()
packer.open("user://output.zip")
packer.start_file("data.json")
packer.write_file(json_bytes)
packer.close_file()
packer.close()
```

> ⚠ Evite: Usar carregamento runtime para recursos do projeto (`res://`) — é menos eficiente e não aproveita o sistema de importação/caching do Godot.

---

## 27. Áudio

### 27.1 Audio Buses

O sistema de áudio usa **buses** (canais de processamento). Qualquer número de buses pode ser criado; cada bus pode ter efeitos em cadeia.

**Escala decibel:**
- `0 dB` = amplitude máxima do hardware — nunca ultrapasse no master bus.
- `-6 dB` = metade da amplitude. `-60 dB` a `-80 dB` = inaudível.
- Trabalhe na faixa `-60 dB` a `0 dB`.

**Hierarquia de buses:**
- Bus **Master** (mais à esquerda) → saída para os alto-falantes.
- Buses adicionais roteiam para outro bus à esquerda deles (sem loops).
- `AudioStreamPlayer` → defina a propriedade `bus` pelo nome (ex.: `"SFX"`, `"Music"`).

**Efeitos disponíveis** (adicionados em Inspector do bus):
`Chorus`, `Delay`, `Reverb`, `Compressor`, `EQ6/10/21`, `Filter` (Low/High/Band Pass/Shelf), `Limiter`, `Panner`, `PitchShift`, `SpectrumAnalyzer`, `Distortion`, etc.

- Godot **desabilita automaticamente** buses silenciosos após alguns segundos (VU meter fica azul).
- Stream Players usam o **nome** do bus — renomear um bus quebra a referência (volta para Master).
- Layout padrão: salvo em `res://default_bus_layout.tres`. Layouts customizados podem ser salvos e carregados via `AudioServer.set_bus_layout()`.

```gdscript
# Ajustar volume de um bus em runtime:
var idx = AudioServer.get_bus_index("Music")
AudioServer.set_bus_volume_db(idx, -20.0)
AudioServer.set_bus_mute(idx, true)
```

### 27.2 AudioStreamPlayer — Tipos e Uso

| Node | Uso |
|---|---|
| `AudioStreamPlayer` | Som não-posicional (música de fundo, UI) |
| `AudioStreamPlayer2D` | Som posicional 2D (panning por posição na tela) |
| `AudioStreamPlayer3D` | Som posicional 3D (panning + atenuação por distância) |

```gdscript
# Reprodução básica:
$AudioStreamPlayer.stream = preload("res://sfx/jump.ogg")
$AudioStreamPlayer.play()
$AudioStreamPlayer.stop()
$AudioStreamPlayer.volume_db = -10.0
$AudioStreamPlayer.pitch_scale = 1.5

# Sinal de fim:
$AudioStreamPlayer.finished.connect(_on_sound_finished)
```

**AudioStreamRandomizer** — variação automática de som:
```gdscript
var randomizer = AudioStreamRandomizer.new()
randomizer.add_stream(0, preload("res://sfx/hit1.ogg"))
randomizer.add_stream(1, preload("res://sfx/hit2.ogg"))
randomizer.random_pitch = 0.1   # variação de pitch ±10%
randomizer.random_volume_offset_db = 3.0
$AudioStreamPlayer.stream = randomizer
$AudioStreamPlayer.play()  # escolhe aleatoriamente a cada play()
```

**AudioStreamPlayer3D — extras:**
- `Area3D` com **Reverb Bus** configurado → sons dentro da área são enviados para bus de reverb específico.
- `Doppler Tracking` → simula efeito Doppler quando emissora/câmera se movem.
- `Uniformity` > 0 → reverb uniforme como em depósitos/cavernas grandes.

**Area2D/3D como zona de áudio:**
- Sons de `AudioStreamPlayer2D/3D` dentro de uma `Area2D/3D` são automaticamente roteados para o bus configurado na Area — permite reverb/efeitos por zona.

### 27.3 Sincronização de Áudio com Gameplay

Para **jogos de ritmo** ou animações sincronizadas com música:

```gdscript
# Método 1 — Relógio do sistema (suficiente para músicas de 2-3 min):
var _time_begin: float
var _time_delay: float

func _ready():
    _time_begin = Time.get_ticks_usec()
    _time_delay = AudioServer.get_time_to_next_mix() + AudioServer.get_output_latency()
    $Player.play()

func _process(_delta):
    var time = (Time.get_ticks_usec() - _time_begin) / 1_000_000.0
    time = maxf(0.0, time - _time_delay)
    # use 'time' para sincronizar visual com áudio
```

```gdscript
# Método 2 — Relógio de hardware (para sessões longas, evita drift):
var _last_mix_time: float
var _last_mix_frames: int

func _ready():
    $Player.play()

func _process(_delta):
    var output_delay = AudioServer.get_output_latency()
    # Atualizar referência a cada mix:
    if AudioServer.get_time_since_last_mix() > 0:
        _last_mix_time = Time.get_ticks_usec() / 1_000_000.0
        _last_mix_frames = $Player.get_playback_position()

    var time = _last_mix_frames + (Time.get_ticks_usec() / 1_000_000.0 - _last_mix_time) - output_delay
    time = maxf(0.0, time)
```

- **Método 1** (relógio de sistema): simples, boa precisão para músicas curtas; drift possível em sessões longas.
- **Método 2** (relógio de hardware via `get_playback_position()`): mais preciso para sessões longas.
- Latência de áudio é configurável em Project Settings → Audio → General → Mix Rate / Latency.

> ⚠ Evite: Usar `AudioStreamPlayer.get_playback_position()` diretamente sem compensação de latência — o valor avança em saltos (por chunk de mix) e chega atrasado nos alto-falantes.

---

## 28. Shaders

### 28.1 Introdução — O que são Shaders

Shaders são programas que rodam na GPU, paralelamente, para cada vértice ou pixel. Diferente de GDScript, **não há estado compartilhado entre execuções** — cada invocação é isolada.

**Funções processor (entry points):**

| Função | Onde roda | Usado em |
|---|---|---|
| `vertex()` | Cada vértice da mesh | `canvas_item`, `spatial` |
| `fragment()` | Cada pixel coberto pela mesh | `canvas_item`, `spatial` |
| `light()` | Cada pixel × cada luz | `canvas_item`, `spatial` |
| `start()` | Cada partícula ao spawnar | `particles` |
| `process()` | Cada partícula por frame | `particles` |
| `sky()` | Pixels do cubemap de radiância + tela | `sky` |
| `fog()` | Froxels de volumetric fog | `fog` |

> ⚠ `light()` não roda se `vertex_lighting` render mode estiver ativo (padrão em mobile) ou se **Force Vertex Shading** estiver habilitado nas Project Settings.

### 28.2 Tipos de Shader e Render Modes

Todo shader começa declarando o tipo na primeira linha:

```glsl
shader_type spatial;      // objetos 3D
shader_type canvas_item;  // objetos 2D, GUI
shader_type particles;    // sistemas de partículas
shader_type sky;          // skies
shader_type fog;          // FogVolumes
```

**Render modes** (segunda linha, opcionais):
```glsl
shader_type spatial;
render_mode unshaded, cull_disabled;
```

Exemplos comuns:

| Render mode | Efeito |
|---|---|
| `unshaded` | Ignora iluminação — cor final vem só do shader |
| `cull_disabled` | Desabilita face culling (ambos os lados visíveis) |
| `blend_mix` | Alpha blending padrão |
| `blend_add` | Additive blending (partículas de fogo, glow) |
| `depth_draw_never` | Nunca escreve no depth buffer |
| `vertex_lighting` | Iluminação calculada por vértice (mais rápido) |

### 28.3 Shading Language — Tipos e Uniforms

**Tipos de dados principais:**

| Tipo | Descrição |
|---|---|
| `bool`, `bvec2/3/4` | Boolean e vetores de bool |
| `int`, `ivec2/3/4` | Integer e vetores de int |
| `float`, `vec2/3/4` | Float e vetores de float |
| `mat2/3/4` | Matrizes (column-major) |
| `sampler2D` | Textura 2D (float) |
| `sampler2DArray` | Array de texturas 2D |
| `samplerCube` | Cubemap |

> ⚠ Variáveis locais **não são inicializadas automaticamente** — atribua um valor antes de usar; uniforms e varyings são inicializados ao padrão.

**Uniforms** — parâmetros expostos ao Inspector e código GDScript:
```glsl
uniform vec4 my_color : source_color = vec4(1.0);  // seletor de cor no Inspector
uniform sampler2D my_texture : source_color;         // textura com hint de cor
uniform float my_value : hint_range(0.0, 1.0) = 0.5;

// Outros hints de textura:
// hint_normal     — textura de normal map
// hint_roughness_* — roughness maps
// filter_nearest  — sem filtragem (pixel art)
// repeat_enable   — UV tiling
```

**Acessar/definir uniforms de GDScript:**
```gdscript
var mat := $MeshInstance3D.get_active_material(0) as ShaderMaterial
mat.set_shader_parameter("my_color", Color.RED)
mat.set_shader_parameter("my_value", 0.75)
```

**Varyings** — interpolados entre vertex() e fragment():
```glsl
varying vec3 world_pos;

void vertex() {
    world_pos = VERTEX;  // passa posição do vértice para fragment
}

void fragment() {
    // world_pos interpolado automaticamente pelo rasterizador
}
```

**Constantes:**
```glsl
const float PI = 3.14159265;
const lowp vec3 DIR = vec3(0.0, 1.0, 0.0);
```

**Precisão** (útil em mobile para performance):
```glsl
lowp vec4 a;    // ~8 bits por componente
mediump vec4 b; // ~16 bits (half float)
highp vec4 c;   // 32 bits (padrão)
```

### 28.4 Primeiro Shader 2D

**Setup:** `Sprite2D` → Inspector → CanvasItem → Material → "New ShaderMaterial" → "New Shader".

**Fragment básico — colorir tudo:**
```glsl
shader_type canvas_item;

void fragment() {
    COLOR = vec4(0.4, 0.6, 0.9, 1.0);
}
```

**Fragment com textura original:**
```glsl
shader_type canvas_item;

void fragment() {
    COLOR = texture(TEXTURE, UV);  // TEXTURE = textura do Sprite2D; UV = coordenada 0-1
}
```

**Efeito de ondulação com vertex():**
```glsl
shader_type canvas_item;
uniform float wave_speed = 3.0;
uniform float wave_amplitude = 5.0;

void vertex() {
    VERTEX.y += sin(VERTEX.x * 0.05 + TIME * wave_speed) * wave_amplitude;
}
```

**Variáveis built-in úteis em canvas_item:**

| Variável | Tipo | Descrição |
|---|---|---|
| `TEXTURE` | `sampler2D` | Textura principal do CanvasItem |
| `UV` | `vec2` | Coordenada UV normalizada (0–1) |
| `COLOR` | `vec4` | Cor de saída em fragment(); cor do vértice em vertex() |
| `VERTEX` | `vec2` | Posição do vértice (modificável em vertex()) |
| `TIME` | `float` | Tempo desde o início (segundos) |
| `SCREEN_UV` | `vec2` | Coordenada UV da tela |

**Variáveis built-in úteis em spatial (3D):**

| Variável | Tipo | Descrição |
|---|---|---|
| `ALBEDO` | `vec3` | Cor difusa base |
| `NORMAL` | `vec3` | Normal da superfície |
| `ROUGHNESS` | `float` | 0 = liso, 1 = rugoso |
| `METALLIC` | `float` | 0 = dielétrico, 1 = metálico |
| `EMISSION` | `vec3` | Cor emissiva (HDR) |
| `ALPHA` | `float` | Transparência (requer render mode blend_mix) |
| `UV`, `UV2` | `vec2` | Coordenadas de textura |

### 28.5 ShaderMaterial vs StandardMaterial3D

- `StandardMaterial3D` = material visual baseado em propriedades (PBR). Pode ser **convertido** para `ShaderMaterial` (clique direito no material → Convert to ShaderMaterial) — gera o código GLSL equivalente.
- `ShaderMaterial` = código shader customizado total.
- Use `StandardMaterial3D` por padrão; converta quando precisar de comportamento que as propriedades padrão não cobrem.

> 💡 Para usar `VisualShader` (editor de nós visual), crie um `ShaderMaterial` → "New VisualShader". O editor de nós gera o código GLSL automaticamente — útil para prototipar efeitos sem escrever GLSL.

---

## 29. Internacionalização (i18n)

### 29.1 Setup: Importar e Registrar Traduções

Registre arquivos de tradução (CSV, `.po`, `.mo`) em **Project > Project Settings > Localization > Translations** (Add / Remove).

Para traduzir o nome do projeto: **Project Settings > Application > Config > Localizable String**.

### 29.2 Detecção Automática e TranslationServer

```gdscript
var language = "automatic"  # carregado das preferências do usuário
if language == "automatic":
    TranslationServer.set_locale(OS.get_locale_language())
else:
    TranslationServer.set_locale(language)
```

**Regra**: use `OS.get_locale_language()` para detectar o idioma preferido do sistema. Se não disponível, Godot usa o Fallback em Project Settings > Internationalization > Locale > Fallback (padrão: `en`).

`TranslationServer` permite adicionar/remover traduções e trocar idioma em runtime.

> ⚠ Evite: hardcodear o idioma padrão sem oferecer opção de troca no jogo.

### 29.3 Tradução de Strings: tr(), tr_n(), Contextos e Pluralização

Controls com `text` traduzem automaticamente se o valor corresponder a uma chave de tradução. Para desabilitar em um nó específico: **Auto Translate > Mode = Disabled** no Inspector.

```gdscript
# Tradução básica
label.text = tr("LEVEL_5_NAME")

# Placeholder nomeado (ordem pode ser trocada pelo tradutor — preferir)
message.text = tr("{personagem} pegou {arma}").format({personagem = "Ogre", arma = "Espada"})

# Placeholder posicional (ordem fixa — pode não funcionar em todos os idiomas)
message.text = tr("%s pegou %s") % ["Ogre", "Espada"]

# Contexto de tradução (desambiguação de strings idênticas com significados diferentes)
button.set_text(tr("Close", "Actions"))    # "fechar" como ação
label.set_text(tr("Close", "Distance"))   # "perto" como distância

# Pluralização
label.text = tr_n("There is %d apple", "There are %d apples", num_apples) % num_apples

# Pluralização com contexto
label.text = tr_n("%d job", "%d jobs", n, "Task Manager") % n
```

**Regra**: prefira placeholders nomeados com `String.format()` para dar liberdade ao tradutor na ordem dos elementos.

### 29.4 CSV (Planilhas)

Formato: primeira coluna = chaves, colunas seguintes = códigos de idioma (`en`, `es`, `ja`). Colunas com prefixo `_` = comentários (não importados).

```csv
keys,en,es,ja
GREET,"Hello, friend!","Hola, amigo!",こんにちは
BYE,Goodbye,Adiós,さようなら
```

Desde Godot 4.6: coluna `?plural` para formas plurais; coluna `?context` para contextos de tradução. Ao usar `?plural` ou `?context`, a tradução automática dos Controls não funciona — use `tr_n()` / `tr()` manualmente.

**Regra**: salvar CSV em UTF-8 **sem BOM**. LibreOffice ou Google Sheets são recomendados (Excel não salva UTF-8 por padrão).

Após importar o CSV (Import dock → Reimport), ainda é necessário registrar em **Localization > Translations**.

### 29.5 gettext (PO/POT)

Vantagens sobre CSV: VCS-friendly (um arquivo por idioma), suporte a multiline, plataformas colaborativas (Transifex, Weblate).

**Criar POT automaticamente:**
Project Settings > Localization > Template Generation → Add cenas/scripts → Generate.

**Criar arquivo `.po` para um idioma:**
```sh
msginit --no-translator --input=messages.pot --locale=fr
```

**Atualizar `.po` após mudanças no POT:**
```sh
# ordem importa: arquivo .po primeiro, depois o .pot
msgmerge --update --backup=none fr.po messages.pot
```

Strings marcadas como "fuzzy" após `msgmerge` não são lidas pelo Godot até serem atualizadas e o comentário removido.

**Validar:**
```sh
msgfmt fr.po --check
```

**Compilar para binário `.mo` (projetos grandes — leitura mais rápida):**
```sh
msgfmt fr.po --no-hash -o fr.mo
msgunfmt fr.mo > fr.po   # descompilar se o .po original for perdido
```

Registrar `.po` ou `.mo` em **Project Settings > Localization > Translations**.

Em GDScript, controle a extração de strings no POT com comentários:
```gdscript
$Label.text = "???"             # NO_TRANSLATE
# TRANSLATORS: Máximo 10 caracteres.
$Button.text = "Tool"
```

### 29.6 Recursos Localizados (Remaps)

Para localizar assets (imagens, áudios) por idioma: **Project Settings > Localization > Remaps** — selecione o recurso base e adicione alternativas por locale.

> ⚠ Evite: usar Remaps para fontes (`DynamicFont`). Use o sistema de **fallback de fontes** do DynamicFont, que funciona independente do idioma ativo e é compatível com multiplayer onde o idioma do texto pode não coincidir com o idioma do cliente.

### 29.7 Bidirectional (BiDi) e RTL

Para idiomas RTL (árabe, hebraico), Godot espelha automaticamente a UI: anchors, alinhamento de texto, ordem dos filhos em containers, e elementos internos de controls (OptionButton, CheckBox, etc.).

Propriedades para sobrescrever em Controls individuais:
- `text_direction`: `LTR`, `RTL`, `Auto` (padrão — segue primeiro caractere forte BiDi)
- `layout_direction`: espelhamento do layout do control
- `structured_text_bidi_override`: para caminhos de arquivo, URIs, e-mails (aplica BiDi por segmento, não ao texto todo)

**Regra**: nós não-UI (Sprites, etc.) não são afetados pelo espelhamento automático — espelhe manualmente ícones de seta que indiquem direção de movimento em idiomas RTL.

Para idiomas sem espaços (tailandês, japonês, khmer): em Project Settings > Internationalization > Locale, habilite **Include Text Server Data** (~4 MB) antes de exportar.

### 29.8 Pseudolocalização

Simula mudanças de localização sem traduções reais para detectar problemas de internacionalização durante o desenvolvimento.

Habilitar: **Project Settings > Internationalization > Pseudolocalization** (com Advanced toggle ativo).

| Propriedade | Efeito |
|---|---|
| `replace_with_accents` | Substitui chars por variantes acentuadas — identifica strings não localizáveis |
| `double_vowels` | Dobra vogais — simula expansão de texto por tradução |
| `fake_bidi` | Simula texto RTL — testa problemas de layout |
| `override` | Substitui tudo por `*` — identifica rapidamente texto não localizado |
| `expansion_ratio` | Padding com `_` (ex: 0.3 = +30%) — testa overflow em containers |
| `skip_placeholders` | Preserva `%s`, `%d`, etc. |

**Runtime:**
```gdscript
ProjectSettings.set_setting("internationalization/pseudolocalization/replace_with_accents", true)
ProjectSettings.set_setting("internationalization/pseudolocalization/double_vowels", true)
TranslationServer.reload_pseudolocalization()
```

**Testar traduções:**
- Editor: **View > Preview Translation** → selecionar idioma
- Project Settings > Internationalization > Locale > **Test** (resetar para vazio antes de commitar!)
- CLI: `godot --language fr`

> ⚠ Evite: commitar o projeto com "Test locale" preenchido — aparece no controle de versão.


---

## 30. Renderers — Visão Geral

### 30.1 Os Três Renderers

| Renderer | Driver | Plataformas | Quando usar |
|---|---|---|---|
| **Forward+** | Vulkan / D3D12 / Metal | Desktop | Jogos 3D com features avançadas |
| **Mobile** | Vulkan / D3D12 / Metal | Mobile + Desktop | Mobile high-end, XR desktop |
| **Compatibility** | OpenGL | Todos (incl. Web) | Hardware antigo, 2D, Web |

- Forward+ tem custo base alto mas escala bem com cenas complexas.
- Compatibility tem custo base baixo mas escala pior (OpenGL forward rendering).
- Trocar de renderer pode exigir ajustes de iluminação e environment — Forward+ ↔ Mobile requer menos ajustes do que qualquer um deles ↔ Compatibility.
- Desde 4.4: se Vulkan não suportado, Forward+/Mobile fazem fallback automático para D3D12, depois para Compatibility.

**Regra**: escolha Compatibility para 2D ou Web; Mobile para mobile high-end; Forward+ para desktop 3D.

**Mobile — Tile-based GPU:**
- GPUs mobile usam tile-based rendering: imagem dividida em tiles processados na memória interna rápida do GPU.
- Sub-passes encadeiam etapas de renderização por tile, reduzindo overhead de leitura/escrita entre passes.
- Leitura da screen texture ou depth texture força write-out completo e interrompe sub-passes — features como Glow, DOF e SSS têm penalidade de performance notável no Mobile renderer quando habilitadas.
- Formato de cor: `R10G10B10A2 UNORM` (metade da largura de banda de `RGBA16F`); HDR limitado por precisão reduzida.

**Compatibility — Iluminação com Sombras:**
- Luzes com sombra são renderizadas em passes adicionais (multi-pass). A mistura de iluminação de sombras ocorre em espaço sRGB (não linear), diferente de Forward+/Mobile — considere ao projetar cenas para Compatibility.

### 30.2 Comparação de Features

| Feature | Compatibility | Mobile | Forward+ |
|---|---|---|---|
| OmniLight/SpotLight máx. | 8 por mesh | 8/mesh, 256/view | 512 por cluster |
| PCSS shadows | ❌ | Omni/Spot ✔ | Todos ✔ |
| Decals | ❌ | ✔ | ✔ |
| VoxelGI / SDFGI | ❌ | ❌ | ✔ |
| SSAO | ✔ (4.6+ simpl.) | ❌ | ✔ (completo) |
| SSR / SSIL | ❌ | ❌ | ✔ |
| Volumetric Fog | ❌ | ❌ | ✔ |
| TAA / FSR2 | ❌ | ❌ | ✔ |
| FXAA / SMAA | ❌ | ✔ | ✔ |
| Compute shaders | ❌ | ✔ (penalidade) | ✔ |
| HDR 2D Viewport | ❌ | ✔ | ✔ |
| CompositorEffects | ❌ | ✔ | ✔ |

---

## 31. Iluminação 3D Avançada

### 31.1 Tipos de Luz 3D

**DirectionalLight3D** — sol/lua; raios paralelos; posição irrelevante; mais barata de calcular.
- `light_angular_distance` > 0 → PCSS (penumbra realista). Caro; use com moderação.

**OmniLight3D** — ponto esférico com `Range` e curva de `Attenuation`.
- `light_size` > 0 → PCSS; sombras via Cube (correto) ou Dual Paraboloid (mais rápido).
- Suporta **projector texture** (formato panorâmico 360°).

**SpotLight3D** — cone com `Angle` e `Angle Attenuation`.
- Sombra mais rápida que Omni (1 textura vs 6/2).
- Suporta projector texture (formato normal, mapeado como decal).

**Propriedades comuns:**
- `light_energy` — multiplicador; use com HDR para valores > 1.
- `light_indirect_energy` — multiplica bounces de GI (LightmapGI, VoxelGI, SDFGI).
- `light_bake_mode` — `DYNAMIC` (tempo real) | `STATIC` (somente baked) | `DISABLED`.
- `light_cull_mask` — camadas que recebem a luz (objetos excluídos ainda castam sombra).
- `distance_fade_enabled` — fade por distância para economizar draw calls.

> ⚠ Evite: colocar mais de 8 DirectionalLights — cada luz extra com sombra divide a resolução do shadow atlas direcional.

### 31.2 Shadow Mapping 3D

**Propriedades de sombra (por luz):**
- `shadow_enabled` — ativa shadow mapping.
- `shadow_bias` / `shadow_normal_bias` — corrige acne/peter-panning; prefira aumentar `normal_bias`.
- `shadow_blur` — suaviza sombras (funciona com PCSS e shadow mapping tradicional).

**DirectionalLight3D — PSSM:**
- Modo padrão: 4 splits (Parallel Split Shadow Maps) para melhor resolução próxima.
- `directional_shadow_max_distance` — reduza para qualidade máxima.
- `directional_shadow_fade_start` (1.0 = sem fade se max_distance cobre toda a cena).
- `directional_shadow_blend_splits` — transição suave entre splits (custo extra).
- `directional_shadow_pancake_size` — corrige sombras faltantes em meshes grandes.

**Shadow filter mode** (Project Settings > Rendering > Lights and Shadows):
- `Soft Low` — padrão, bom para texturas detalhadas.
- `Soft Medium/High/Ultra` — mais suave; necessário em jogos com arte simples.

**Shadow map size** — padrão 4096; reduza para 2048 em GPUs low-end.

**PCF — Padrão Vogel Disk:**
- Forward+ e Mobile usam padrão **vogel disk** para PCF (não padrão fixo) — permite ajuste suave do número de amostras e qualidade.
- O kernel PCF é rotacionado por pixel para suavizar artefatos de under-sampling.
- PCSS (sombras com penumbra física via `light_size`/`light_angular_distance`) está disponível apenas no Forward+ renderer por custo de GPU.

### 31.3 Shadow Atlas (OmniLight / SpotLight)

Todas as sombras posicionais compartilham um **shadow atlas** (4 quadrantes subdivididos).
- Padrão: 4 + 4 + 16 + 64 = até 88 luzes com sombra simultâneas.
- Se atlas lotado, algumas luzes não renderizam sombra.
- Configure em Project Settings > Rendering > Lights and Shadows > Positional Shadow.

**Regra**: use `light_bake_mode = STATIC` + LightmapGI para luzes estáticas — economiza atlas e melhora performance.

---

## 32. Environment e Post-Processing

### 32.1 WorldEnvironment e CameraAttributes

**WorldEnvironment** — nó recomendado; apenas um por scene tree; pode ser sobrescrito por camera.
**Camera3D.environment** — prioridade máxima, sobrescreve WorldEnvironment.
**CameraAttributes** — armazena exposure e depth of field separadamente do Environment.
- `CameraAttributesPractical` — unidades arbitrárias (mais simples para jogos).
- `CameraAttributesPhysical` — unidades reais (mm focal, EV100); bloqueia FOV da Camera3D.

**Regra**: atribua CameraAttributes na Camera3D, não no WorldEnvironment — evita DOF no editor.

### 32.2 Background, Sky Materials e Ambient Light

**Modos de background:**
- `Clear Color` / `Custom Color` — cor sólida.
- `Sky` — sky material (IBL: afeta reflexos e luz ambiente mesmo sem estar visível).
- `Canvas` — cena 2D como fundo (útil para glow em 2D).
- `Keep` — reutiliza frame anterior (cenas indoor sem visão do céu).

**Sky Materials:**
- `PanoramaSkyMaterial` — HDRI 2:1; use `.hdr`/`.exr` para HDR; ative "HDR Clamp Exposure" para evitar sparkles.
- `ProceduralSkyMaterial` — céu procedural; posição do sol derivada de até 4 DirectionalLight3D.
- `PhysicalSkyMaterial` — parâmetros físicos de scattering; apenas 1 sol.

**Ambient light:**
- `Background` — intensidade varia com o sky (mais realista).
- `Color` — constante em todas as direções (mais flat, mais rápido).
- `Sky Contribution` (0–1) — blend entre cor ambiente e sky.

**Reflected light (specular IBL):** Background | Disabled | Sky.

### 32.3 Tonemapping

| Modo | Característica |
|---|---|
| `Linear` | Sem modificação; clipa highlights; mais rápido |
| `Reinhard` | Evita clipping; pode parecer apagado |
| `Filmic` | Melhor contraste que Reinhard |
| `ACES` | Alto contraste; dessatura highlights |
| `AgX` | Mantém hue ao ficar mais brilhante; mais lento |

- `exposure` — multiplicador de brilho antes do tonemapper.
- `white` — ponto de referência para branco (6–8 para PBR realista).

### 32.4 Screen-Space Effects (SSR, SSAO, SSIL)

**SSR (Screen-Space Reflections)** — Forward+ only.
- Reflexos em tempo real para superfícies em contato; complementa ReflectionProbe.
- Não reflete geometria transparente (não grava no depth buffer).
- `half_size` (Project Settings) — padrão true; desative para qualidade máxima.

**SSAO (Screen-Space Ambient Occlusion)** — Forward+ e Compatibility (4.6+ simplificado).
- Escurece áreas côncavas/oclusas na luz ambiente — **não afeta luz direta** por padrão.
- `light_affect` > 0 → aplica também em luz direta (não físico, mas usado artisticamente).
- Qualidade: Radius, Intensity, Power, Detail, Half Size, Adaptive Target em Project Settings.

**SSIL (Screen-Space Indirect Lighting)** — Forward+ only.
- Complemento a VoxelGI/SDFGI/LightmapGI para detalhes dinâmicos e emissivos.
- Não é SSGI completo — apenas iluminação indireta por screen-space.

> ⚠ Evite: habilitar SSR + SSAO + SSIL simultaneamente sem validar performance; cada um tem custo de GPU significativo.

### 32.5 Glow e Fog

**Glow** — simula bleeding de luz em câmeras/filmes.
- Aparece quando pixel ultrapassa `hdr_threshold` OU `bloom` > 0.
- Blend modes: `Additive` (forte), `Screen` (equilibrado), `Softlight` (sutil), `Replace` (debug/blur), `Mix`.
- `Levels` — tamanho e forma do glow (menor = local, maior = difuso na tela).
- **Glow como blur de tela**: `normalized=true`, `intensity=1.0`, `bloom=1.0`, blend=`Replace`, `hdr_luminance_cap=1.0`.
- Glow em 2D: habilite `Rendering > Viewport > HDR 2D` e ajuste `Modulate > Intensity` nos sprites.

**Fog (não-volumétrico):**
- `Depth Fog` — baseado em distância da câmera.
- `Height Fog` — baseado em altitude, independente de distância.
- `sun_scatter` — tinge fog com cor do DirectionalLight (simula pôr do sol).
- `aerial_perspective` — tinge fog com cor do sky (blend natural horizonte/fundo).

**Volumetric Fog** — Forward+ only; cor afetada por luzes que atravessam o volume. Configure `FogVolume` nodes para áreas localizadas.

### 32.6 TAA e FSR 2.2

**TAA (Temporal Anti-Aliasing)** — Forward+ only.
- Requer motion vectors corretos por objeto — motion vectors ausentes ou incorretos causam **ghosting** quando câmera ou objetos se movem.
- Motion vectors gerados no vertex shader principal (diferença entre posição no frame atual e no frame anterior).

**FSR 2.2** — upscaling com TAA integrado (Forward+ only).
- Renderiza em resolução menor e faz upscale temporal, combinando upscaling e anti-aliasing em um único passo.
- Alternativa ao TAA nativo quando upscaling de resolução é necessário.
- Habilite em Project Settings > Rendering > Scaling 3D > Scale Mode: FSR2.

**Regra**: prefira FSR 2.2 ao TAA nativo quando precisar de upscaling — combina as duas funcionalidades sem custo duplo.

---

## 33. Luzes e Sombras 2D

### 33.1 Nodes de Iluminação 2D

Cenas 2D são não-shaded por padrão. Para iluminação real-time 2D:

| Node | Função |
|---|---|
| `CanvasModulate` | Define cor ambiente base (áreas sem luz ficam com essa cor) |
| `PointLight2D` | Luz omnidirecional ou spot via textura |
| `DirectionalLight2D` | Luz solar/lunar com raios paralelos |
| `LightOccluder2D` | Caster de sombra (polígono oclusor) |

**Regra**: sempre adicione `CanvasModulate` — sem ele, as luzes apenas adicionam brilho ao render já totalmente iluminado.

### 33.2 PointLight2D e DirectionalLight2D

**PointLight2D:**
- `texture` — define tamanho e forma da luz (use `GradientTexture2D` radial para falloff customizado).
- `texture_scale` — multiplica tamanho; luzes maiores custam mais GPU.
- `height` — altura virtual para normal mapping (aumente se usar normal maps).
- `blend_mode`: `Add` (padrão), `Subtract` (luz negativa), `Mix` (blend linear).
- `range_z_min/max`, `range_layer_min/max` — filtra camadas Z e layers afetadas.

**DirectionalLight2D:**
- `height` (0.0–1.0) — ângulo para normal mapping; não afeta sombras.
- `max_distance` — câmeras afastadas não castam sombra além desse pixel.
- Sombras direcionais são sempre infinitamente longas (limitação do método 2D).

### 33.3 LightOccluder2D e Sombras

Para sombras aparecerem: luz com `shadow_enabled = true` + `LightOccluder2D` com polígono definido.

**Criar oclusor automaticamente**: selecione Sprite2D → menu Sprite2D → *Create LightOccluder2D Sibling*.
**Criar manualmente**: adicione `LightOccluder2D`, clique "+" no editor 2D para criar polígono.

**Propriedades de sombra na luz:**
- `shadow_color` — cor/opacidade das áreas sombreadas.
- `shadow_filter`: `None` (pixel art), `PCF5` (suave), `PCF13` (mais suave, mais caro).
- `shadow_filter_smooth` — suavidade; valores altos causam banding.
- `shadow_item_cull_mask` — controla quais `LightOccluder2D` castam sombra para esta luz.

**Pixel art com sombras pixeladas**: use shader para snap de `LIGHT_VERTEX` e `SHADOW_VERTEX`:

```gdshader
shader_type canvas_item;
uniform float pixel_size = 4.0;
void fragment() {
    LIGHT_VERTEX.xy = floor(LIGHT_VERTEX.xy / pixel_size) * pixel_size;
    SHADOW_VERTEX = floor(SHADOW_VERTEX / pixel_size) * pixel_size;
    COLOR = texture(TEXTURE, UV);
}
```

### 33.4 Normal e Specular Maps em 2D

Atribua `CanvasTexture` ao campo de textura do node (ex.: Sprite2D):
- `diffuse_texture` — textura de cor base.
- `normal_map_texture` — normal map (use Laigter para gerar de height map).
- `specular_texture` — mapa de intensidade especular (geralmente grayscale).
- `specular_color` / `specular_shininess` — cor e expoente das reflexões.

Após habilitar normal map, aumente `height` em PointLight2D/DirectionalLight2D para ver o efeito.

**Alternativa performática**: `Sprite2D` com `CanvasItemMaterial` em modo `Blend Add` simula luzes sem pipeline separado — mais rápido, mas sem sombras e sem normal/specular maps.

---

## 34. GDExtension

### 34.1 O que é GDExtension

GDExtension permite ao Godot interagir com **shared libraries nativas em runtime** sem recompilar o engine. Usado para:
- Bindings de outras linguagens (C++, Rust, Swift etc.).
- Integração de bibliotecas C/C++ de terceiros.
- Performance crítica em código nativo.

Três componentes centrais:
1. `gdextension_interface.h` — funções C para comunicação engine ↔ extension (obtenha com `godot --dump-gdextension-interface`).
2. `extension_api.json` — APIs Godot expostas (obtenha com `godot --dump-extension-api`).
3. `*.gdextension` — arquivo lido pelo Godot para carregar a extensão.

A maioria usa **godot-cpp** (binding oficial C++) em vez da API C diretamente.

**Compatibilidade de versão:**
- `compatibility_minimum` — impede versões antigas de carregar.
- `compatibility_maximum` — impede versões futuras (se necessário).

### 34.2 Arquivo .gdextension — Estrutura

```ini
[configuration]
entry_symbol = "example_library_init"   ; função de inicialização obrigatória
compatibility_minimum = "4.2"
reloadable = true                        ; recarrega ao recompilar (dev only)

[libraries]
; Feature flags: SO.build.arch — avaliados top-to-bottom, primeiro match vence
; Entries mais específicos devem vir ANTES dos genéricos
macos.debug   = "./bin/libexample.macos.template_debug.dylib"
macos.release = "./bin/libexample.macos.template_release.dylib"
windows.debug.x86_64   = "./bin/libexample.windows.template_debug.x86_64.dll"
windows.release.x86_64 = "./bin/libexample.windows.template_release.x86_64.dll"
linux.debug.x86_64     = "./bin/libexample.linux.template_debug.x86_64.so"
linux.release.x86_64   = "./bin/libexample.linux.template_release.x86_64.so"

[icons]
MyCustomNode = "res://icons/my_node.svg"   ; SVG 16x16; ative Scale+Convert no Import dock

[dependencies]
; Dependências extras copiadas no export
windows.release = {
    "res://bin/libdependency.dll" : ""
}
macos.release = {
    "res://bin/libdep.framework" : "Contents/Frameworks"
}
```

**Feature flags disponíveis:**
- SO: `windows`, `macos`, `linux`, `android`, `ios`, `web`
- Build: `debug`, `release`, `editor`
- Arch: `x86_64`, `arm64`, `rv64`, `wasm32`, `double` (double-precision)

**Regra**: use caminhos relativos nas libraries — a extensão funcionará mesmo instalada em diretório diferente.

> ⚠ Evite: `reloadable = true` em builds de release — é para desenvolvimento apenas.

---

## 35. Editor Plugins

### 35.1 Plugin Básico — Estrutura e Ciclo de Vida

Um **editor plugin** é uma ferramenta que estende o editor Godot usando GDScript. Não requer C++ nem recompilação.

**Localização padrão:** `res://addons/<plugin_name>/`

Dois arquivos obrigatórios:
1. `plugin.cfg` — metadados (nome, descrição, versão, script principal)
2. Script `@tool` herdando `EditorPlugin`

```ini
[plugin]
name="My Plugin"
description="Extends the editor."
author="Your Name"
version="1.0"
script="my_plugin.gd"
```

```gdscript
@tool
extends EditorPlugin

func _enter_tree():
    # inicialização — chamado quando o plugin é ativado
    pass

func _exit_tree():
    # limpeza — chamado quando o plugin é desativado
    pass
```

**Regra**: Todo script usado pelo plugin (exceto o `EditorPlugin` principal) também deve ser `@tool`, caso contrário age como arquivo vazio no editor.

**Ativar:** Project Settings → Plugins → habilitar a checkbox do plugin.

### 35.2 Custom Node (nó customizado)

Adiciona um novo tipo de nó disponível em "Add Node":

```gdscript
@tool
@icon("icon.png")           # ícone 16×16; opcional
class_name MyButton
extends Button

func _enter_tree():
    pressed.connect(clicked)

func clicked():
    print("You clicked me!")
```

- O `class_name` registra automaticamente o nó no diálogo "Create New Node".
- Ícones SVG devem ter as opções **Scale With Editor Scale** e **Convert Colors With Editor Theme** ativas no Import dock.

### 35.3 Custom Dock (painel customizado)

Adiciona um dock à interface do editor:

```gdscript
@tool
extends EditorPlugin

var dock

func _enter_tree():
    var dock_scene = preload("res://addons/my_dock/my_dock.tscn").instantiate()
    dock = EditorDock.new()
    dock.add_child(dock_scene)
    dock.title = "My Dock"
    dock.default_slot = DOCK_SLOT_LEFT_UL
    dock.available_layouts = EditorDock.DOCK_LAYOUT_VERTICAL | EditorDock.DOCK_LAYOUT_FLOATING
    add_dock(dock)

func _exit_tree():
    remove_dock(dock)
    dock.queue_free()
```

- A cena do dock deve ter um `Control` como raiz.
- O usuário pode mover o dock livremente; o layout é salvo entre sessões.

### 35.4 Main Screen Plugin (aba central)

Adiciona uma aba junto a "2D", "3D", "Script":

```gdscript
@tool
extends EditorPlugin

const MainPanel = preload("res://addons/my_plugin/main_panel.tscn")
var main_panel_instance

func _enter_tree():
    main_panel_instance = MainPanel.instantiate()
    EditorInterface.get_editor_main_screen().add_child(main_panel_instance)
    _make_visible(false)   # obrigatório — ocultar ao ativar

func _exit_tree():
    if main_panel_instance:
        main_panel_instance.queue_free()

func _has_main_screen() -> bool:
    return true

func _make_visible(visible: bool):
    if main_panel_instance:
        main_panel_instance.visible = visible

func _get_plugin_name() -> String:
    return "My Screen"

func _get_plugin_icon() -> Texture2D:
    return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")
```

**Regra**: Chame `_make_visible(false)` logo após `add_child()` — sem isso a aba aparecerá visível ao ativar o plugin.

### 35.5 Registrando Autoloads em Plugins

```gdscript
@tool
extends EditorPlugin

const AUTOLOAD_NAME = "SomeAutoload"

func _enable_plugin():
    add_autoload_singleton(AUTOLOAD_NAME, "res://addons/my_addon/some_autoload.tscn")

func _disable_plugin():
    remove_autoload_singleton(AUTOLOAD_NAME)
```

### 35.6 Sub-plugins

Permite dividir um plugin em vários EditorPlugins independentes organizados numa pasta:

```
addons/my_plugin/
    plugin.cfg          ← plugin principal
    plugin.gd           ← script principal
    node/plugin.cfg     ← sub-plugin (oculto na lista)
    panel/plugin.cfg    ← sub-plugin (oculto na lista)
```

```gdscript
@tool
extends EditorPlugin

const PLUGIN_NAME = "my_plugin"

func _enable_plugin():
    EditorInterface.set_plugin_enabled(PLUGIN_NAME + "/node", true)
    EditorInterface.set_plugin_enabled(PLUGIN_NAME + "/panel", true)

func _disable_plugin():
    EditorInterface.set_plugin_enabled(PLUGIN_NAME + "/node", false)
    EditorInterface.set_plugin_enabled(PLUGIN_NAME + "/panel", false)
```

### 35.7 Import Plugin (EditorImportPlugin)

Permite importar formatos de arquivo customizados como recursos nativos do Godot.

**Estrutura mínima:**

```gdscript
# import_plugin.gd
@tool
extends EditorImportPlugin

func _get_importer_name():   return "demos.myformat"
func _get_visible_name():    return "My Format"
func _get_recognized_extensions(): return ["myfmt"]
func _get_save_extension():  return "res"
func _get_resource_type():   return "Resource"
func _get_preset_count():    return 1
func _get_preset_name(i):    return "Default"

func _get_import_options(path, preset_index):
    return [{"name": "my_option", "default_value": false}]

func _get_option_visibility(path, option_name, options):
    return true

func _import(source_file, save_path, options, r_platform_variants, r_gen_files):
    var res = Resource.new()
    # ... lógica de leitura e criação do recurso ...
    return ResourceSaver.save(res, "%s.%s" % [save_path, _get_save_extension()])
```

Registrar no `EditorPlugin` principal:

```gdscript
var import_plugin

func _enter_tree():
    import_plugin = preload("import_plugin.gd").new()
    add_import_plugin(import_plugin)

func _exit_tree():
    remove_import_plugin(import_plugin)
    import_plugin = null
```

**r_platform_variants** — variantes por plataforma (feature tags antes da extensão):
```gdscript
r_platform_variants.push_back("mobile")
ResourceSaver.save(mobile_res, "%s.mobile.%s" % [save_path, _get_save_extension()])
```

**r_gen_files** — arquivos extras gerados (dependências):
```gdscript
r_gen_files.push_back(extra_path)
```

### 35.8 Inspector Plugin (EditorInspectorPlugin + EditorProperty)

Substitui ou adiciona controles no Inspector para tipos ou propriedades específicas.

```gdscript
# my_inspector_plugin.gd
extends EditorInspectorPlugin

func _can_handle(object) -> bool:
    return true   # trata todos os objetos

func _parse_property(object, type, name, hint_type, hint_string, usage_flags, wide) -> bool:
    if type == TYPE_INT:
        add_property_editor(name, RandomIntEditor.new())
        return true   # remove o editor padrão
    return false
```

```gdscript
# random_int_editor.gd — widget customizado
extends EditorProperty

var property_control = Button.new()
var current_value = 0
var updating = false

func _init():
    add_child(property_control)
    add_focusable(property_control)
    refresh_control_text()
    property_control.pressed.connect(_on_button_pressed)

func _on_button_pressed():
    if updating: return
    current_value = randi() % 100
    refresh_control_text()
    emit_changed(get_edited_property(), current_value)

func _update_property():
    var new_value = get_edited_object()[get_edited_property()]
    if new_value == current_value: return
    updating = true
    current_value = new_value
    refresh_control_text()
    updating = false

func refresh_control_text():
    property_control.text = "Value: " + str(current_value)
```

**Posicionamento:**
- `add_child(control)` — à direita do nome da propriedade.
- `add_child(control)` + `set_bottom_editor(control)` — abaixo do nome.

### 35.9 Visual Shader Plugin (VisualShaderNodeCustom)

Cria nós customizados no editor de VisualShader — **não precisa de `plugin.cfg`**, basta `class_name`:

```gdscript
@tool
extends VisualShaderNodeCustom
class_name VisualShaderNodeMyNoise

func _get_name():        return "MyNoise"
func _get_category():    return "MyAddons"
func _get_description(): return "Custom noise node"

func _get_return_icon_type():
    return VisualShaderNode.PORT_TYPE_SCALAR

func _get_input_port_count():  return 1
func _get_input_port_name(port):  return "uv"
func _get_input_port_type(port):  return VisualShaderNode.PORT_TYPE_VECTOR_3D

func _get_output_port_count(): return 1
func _get_output_port_name(port):  return "result"
func _get_output_port_type(port):  return VisualShaderNode.PORT_TYPE_SCALAR

func _get_code(input_vars, output_vars, mode, type):
    return output_vars[0] + " = " + input_vars[0] + ".x;"
```

### 35.10 3D Gizmo Plugin (EditorNode3DGizmoPlugin)

Cria gizmos customizados para nós `Node3D`:

```gdscript
# my_gizmo_plugin.gd
extends EditorNode3DGizmoPlugin

func _get_gizmo_name(): return "MyNode3D"

func _init():
    create_material("main", Color(1, 0, 0))
    create_handle_material("handles")

func _has_gizmo(node):
    return node is MyCustomNode3D

func _redraw(gizmo):
    gizmo.clear()
    var node3d = gizmo.get_node_3d()
    var lines = PackedVector3Array([
        Vector3(0, 1, 0),
        Vector3(0, node3d.my_value, 0)
    ])
    gizmo.add_lines(lines, get_material("main", gizmo), false)
```

Registrar no `EditorPlugin`:

```gdscript
var gizmo_plugin = MyGizmoPlugin.new()

func _enter_tree():
    add_node_3d_gizmo_plugin(gizmo_plugin)

func _exit_tree():
    remove_node_3d_gizmo_plugin(gizmo_plugin)
```

> ⚠ Evite: Scripts usados pelo plugin sem `@tool` — eles são tratados como arquivos vazios pelo editor.

---

## 36. Múltiplas Resoluções

### 36.1 Conceito — Base Size e Viewport

O Godot **nunca muda a resolução do monitor**. Em vez disso, renderiza para uma viewport (base size) e escala para o tamanho da janela.

- **Base size** (`Project Settings → Display → Window`): o "tamanho de design", equivalente ao retângulo azul no editor 2D.
- **Window**: área de tela fornecida pelo SO ao jogo.
- **Viewport** (`get_tree().root`): o objeto que o jogo preenche; uma instância `Window`.

Configurar em runtime:
```gdscript
get_tree().root.content_scale_size   # base size (Window.content_scale_size)
get_tree().root.content_scale_mode   # stretch mode
get_tree().root.content_scale_aspect # stretch aspect
get_tree().root.content_scale_factor # stretch scale
```

### 36.2 Stretch Mode

| Modo | Comportamento |
|---|---|
| `disabled` (padrão) | Sem stretching — 1 unidade = 1 pixel. |
| `canvas_items` | A base size é esticada para cobrir a janela. Tudo renderizado em resolução final. 2D pode ter artefatos de escala. |
| `viewport` | A viewport tem exatamente a base size. A cena é renderizada nessa viewport, depois escalada para a janela. |

### 36.3 Stretch Aspect

Válido somente quando Stretch Mode ≠ `disabled`:

| Aspect | Comportamento |
|---|---|
| `ignore` | Distorce para preencher toda a tela (aspecto pode mudar). |
| `keep` | Mantém aspecto — adiciona barras pretas (letterbox/pillarbox). |
| `keep_width` | Mantém largura; expande verticalmente em telas mais altas. |
| `keep_height` | Mantém altura; expande horizontalmente em telas mais largas. |
| `expand` | Mantém aspecto; expande em ambas as direções conforme a tela. |

### 36.4 Stretch Scale e Scale Mode

**Scale** (`content_scale_factor`): fator multiplicador adicional sobre o stretch.
- Com `disabled`: 1 unidade = `scale` pixels.
- Com `canvas_items`: elementos 2D escalam a partir da base size × scale.
- Com `viewport`: a resolução da viewport é dividida pelo scale (mais pixels visíveis por unidade).

**Scale Mode** (desde Godot 4.2):
- `fractional` (padrão): qualquer fator é permitido (ex.: 2.133×).
- `integer`: arredonda para baixo ao inteiro mais próximo (ex.: 2×) — essencial para **pixel art** evitar escalonamento irregular.

**Regra**: Use `Exclusive Fullscreen` (não `Fullscreen`) para jogos. O modo `Fullscreen` deixa uma linha de 1px na base da tela, podendo forçar um scale integer menor que o esperado.

### 36.5 Recomendações por Cenário

**Desktop — não pixel art:**
```
Stretch Mode:   canvas_items
Stretch Aspect: expand
Base Size:      1920×1080 (ou 3840×2160 para high-end)
```
- Use anchors nos `Control` para bordas da tela.
- Considere expor "Resolution Scaling" para jogos 3D.

**Desktop — pixel art:**
```
Stretch Mode:   viewport
Stretch Aspect: keep (aspecto fixo) ou expand
Scale Mode:     integer
Base Size:      640×360 (escala perfeita para 720p/1080p/1440p/4K)
```

**Mobile landscape:**
```
Stretch Mode:   canvas_items
Stretch Aspect: expand
Base Size:      1280×720 (ou 1920×1080)
```
- `GUI > Theme > Default Theme Scale`: 1.5–2.0 para telas densas.

**Mobile portrait:**
```
Stretch Mode:   canvas_items
Stretch Aspect: expand
Base Size:      720×1280
Orientation:    portrait (Display > Window > Handheld)
```

**Aplicação não-jogo:**
```
Stretch Mode:   disabled
Stretch Aspect: keep (ignorado)
```
- Defina `get_window().min_size` no `_ready()` para evitar layout quebrado.
- Exponha slider de escala usando `content_scale_factor`.

### 36.6 hiDPI

- Projeto DPI-aware por padrão (`Display > Window > DPI > Allow hiDPI` = true). **Não desative** — quebra fullscreen no Windows.
- Em hiDPI a janela inicial aparece pequena; a solução mais comum é forçar fullscreen.
- Para apps não-jogo: leia `DisplayServer.screen_get_scale()` no `_ready()` de um autoload e defina `content_scale_factor` correspondente.

```gdscript
# autoload DpiHelper.gd
func _ready():
    var scale = DisplayServer.screen_get_scale()
    get_tree().root.content_scale_factor = scale
```

> ⚠ Evite: Usar `Fullscreen` em vez de `Exclusive Fullscreen` em jogos — especialmente com integer scale, pois a linha de 1px pode forçar um fator menor.

### 36.7 Campo de Visão 3D em Múltiplos Aspectos

- Câmera 3D: `Keep Aspect = Keep Height` (Hor+) — padrão, melhor para landscape/desktop.
- Para portrait: use `Keep Width` (Vert-) — telas 19:9 ganham campo de visão vertical.

> ⚠ Evite: Esperar que resolução e aspect ratio sejam fixos — sempre configure stretch mode + aspect e use anchors nos Controls.

---

## 37. @tool — Executando Código no Editor

### 37.1 O que é `@tool`

Adicionar `@tool` no topo de um script faz com que ele execute **dentro do editor** (além de em runtime). Útil para:
- Visualizar trajetórias de física / alturas de pulo no editor.
- Fazer personagens que se desenham por código aparecerem na viewport do editor.
- Gerar/modificar nodes automaticamente ao editar propriedades.

> ⚠ Danger: Scripts `@tool` acessam a scene tree do editor. `Node.queue_free()` pode causar crash se o editor estiver processando o node. Sempre verifique o contexto com `Engine.is_editor_hint()`.

### 37.2 Uso Básico

```gdscript
@tool
extends Sprite2D

func _process(delta):
    if Engine.is_editor_hint():
        rotation += PI * delta   # só no editor
    else:
        rotation -= PI * delta   # só em game
    # código sem guard roda em ambos
```

- **Regra**: Separe sempre código de editor de código de jogo com `Engine.is_editor_hint()`.
- Todo script GDScript que seu `@tool` **usa** também precisa de `@tool`. Métodos estáticos e constantes são exceção — podem ser chamados de qualquer script.
- `extends @tool` não herda o comportamento de tool; o script filho precisa declarar `@tool` explicitamente.

### 37.3 Propriedades Exportadas com Setter

```gdscript
@tool
extends Sprite2D

@export var speed = 1:
    set(new_speed):
        speed = new_speed
        rotation = 0   # reseta ao editar no inspector
```

- **Regra**: Chame `update_configuration_warnings()` dentro de setters de propriedades que afetam o aviso de configuração do node.

### 37.4 Aviso de Configuração do Node

```gdscript
@export var title = "":
    set(p_title):
        title = p_title
        update_configuration_warnings()

func _get_configuration_warnings() -> PackedStringArray:
    var warnings: PackedStringArray = []
    if title == "":
        warnings.append("Defina `title` com um valor não-vazio.")
    return warnings   # vazio = sem aviso
```

### 37.5 Monitorar Mudanças em Resources

Por padrão, o setter do `@tool` não é chamado quando propriedades do resource são alteradas no inspector. Solução: conectar o sinal `changed` do resource.

```gdscript
@export var resource: MyResource:
    set(new_resource):
        if resource != null:
            resource.changed.disconnect(_on_resource_changed)
        resource = new_resource
        if resource != null:
            resource.changed.connect(_on_resource_changed)

func _on_resource_changed():
    pass  # reage à mudança
```

O resource também precisa de `@tool` e emitir `changed.emit()` nos seus setters.

### 37.6 EditorScript — Scripts One-off

Para tarefas pontuais (não plugins), estenda `EditorScript` em vez de usar um plugin completo.

```gdscript
@tool
class_name ScaleOmniLights
extends EditorScript

func _run():
    for node in EditorInterface.get_edited_scene_root().find_children("", "OmniLight3D"):
        var is_subscene_child = node != get_scene() and node.owner != get_scene()
        if not is_subscene_child:
            node.omni_range *= 2.0
            EditorInterface.mark_scene_as_unsaved()
```

Formas de executar:
- `File > Run` no editor de script (aba ativa).
- `Ctrl+Shift+X` com o script na aba ativa.
- Clique direito no FileSystem dock → **Run**.
- `Ctrl+Shift+P` → nome da classe (requer `class_name`).

> ⚠ Danger: EditorScripts não têm undo/redo. Salve a cena antes de rodar scripts que modificam dados.

### 37.7 Instancing de Scenes no Editor

```gdscript
# @tool script
func _ready():
    var node = Node3D.new()
    add_child(node)
    # Obrigatório para aparecer no dock e persistir no arquivo .tscn:
    node.owner = get_tree().edited_scene_root

# EditorScript
func _run():
    var parent = get_scene().get_node("Parent")
    var node = Node3D.new()
    parent.add_child(node)
    node.owner = get_scene()
```

- **Regra**: Defina `node.owner` para o root da scene editada; sem isso o node some ao fechar a scene.

### 37.8 Debug

O debugger e breakpoints não funcionam diretamente em scripts `@tool`. Alternativas:
- Use `print()` — saída aparece no painel Output do editor.
- Abra uma segunda instância do editor via **Debug > Customize Run Instances...** com `--editor` em *Main Run Args*.

> ⚠ Evite: Modificações feitas por `@tool` não têm undo. Use controle de versão (Git) antes de testar scripts que alteram a scene.

---

## 38. Viewports

### 38.1 Visão Geral

| Tipo | Descrição |
|---|---|
| `Window` (Root Viewport) | Viewport principal; projetada numa janela do OS. |
| `SubViewport` | Viewport secundária adicionada à scene; renderiza para uma textura (*render target*). |

Casos de uso de `SubViewport`:
- Renderizar objetos 3D num jogo 2D (e vice-versa).
- Gerar texturas dinâmicas / procedurais em runtime.
- Múltiplas câmeras na mesma scene.
- Minimaps, espelhos, UI 3D.

### 38.2 SubViewport como Render Target

```gdscript
# Aplicar conteúdo do SubViewport como textura
var tex = $SubViewport.get_texture()
$Sprite2D.texture = tex
```

No editor: selecione a propriedade de textura → **New ViewportTexture** → escolha o SubViewport.

**Clear Mode:**

| Modo | Comportamento |
|---|---|
| `Always` (padrão) | Limpa todo frame com a cor de fundo (ou transparente se `Transparent BG` = true). |
| `Never` | Nunca limpa — acumulação de frames. |
| `Next Frame` | Limpa no próximo frame, depois muda para `Never`. |

**Update Mode:**

| Modo | Comportamento |
|---|---|
| `Always` | Re-renderiza todo frame. |
| `Once` | Re-renderiza um frame, depois muda para `Never` — update manual. |
| `Never` | Nunca re-renderiza. |
| `When Parent Visible` | Re-renderiza apenas quando o SubViewport está visível. |

- **Regra**: Se o conteúdo é estático, use `Update Mode = Once` depois de setar — economiza custo de renderização por frame.

### 38.3 Input e Listener

- `SubViewport` não recebe input por padrão — apenas quando é filho direto de `SubViewportContainer`.
- Desative input no container com a propriedade **Disable Input**.
- Para som 3D espacial dentro de um SubViewport, habilite **Audio Listener Enable 3D** (ou 2D) na propriedade do SubViewport.

### 38.4 Câmeras

- Cada câmera renderiza no `Viewport` pai mais próximo na hierarquia.
- Pode haver apenas uma câmera ativa por Viewport — defina `camera.make_current()` se houver mais de uma.
- Câmeras 3D: use `cull_mask` + `VisualInstance3D.layers` para filtrar quais objetos renderizar por viewport.

### 38.5 Worlds (2D e 3D)

- Por padrão, um SubViewport **compartilha** o `World3D` do Viewport pai.
- Para isolar física/renderização: defina **World 3D** no SubViewport (cria um universo separado).
- **Own World3D**: flag que cria um World3D isolado automaticamente — útil para instanciar personagens 3D dentro de uma UI 2D.
- Cada Viewport sempre tem seu próprio `World2D`; compartilhamento é possível via `world_2d` por código.

### 38.6 Captura de Tela (Screenshot)

```gdscript
# Esperar o frame terminar antes de capturar
await RenderingServer.frame_post_draw
var img = get_viewport().get_texture().get_image()
var tex = ImageTexture.create_from_image(img)
sprite.texture = tex
```

> ⚠ Evite: Chamar `get_image()` em `_ready()` ou no primeiro frame — retorna textura vazia pois nada foi renderizado ainda.

### 38.7 SubViewportContainer

- SubViewport filho de `SubViewportContainer` torna-se ativo automaticamente.
- `Stretch = true` no container faz o SubViewport cobrir toda a área do container.
- O container não pode ser menor que o SubViewport.

### 38.8 Opções de Renderização

| Opção | Efeito |
|---|---|
| **MSAA** | Nível de anti-aliasing independente por viewport. |
| **Disable 3D** | Levemente mais rápido e menos memória quando o viewport só usa 2D. |
| **Debug Draw** | `Unshaded`, `Overdraw`, `Wireframe` — útil para diagnóstico. |
| `positional_shadow_atlas_size` | Defina > 0 para sombras funcionarem no viewport (padrão: 4096 desktop / 2048 mobile). |

> ⚠ Evite: Esperar que `Debug Draw` funcione no renderer Compatibility — não é suportado; os modos aparecem como draw normal.

---

## 39. Compositor e Custom Post-Processing

### 39.1 Compositor — Visão Geral

O **Compositor** (Godot 4) controla o pipeline de renderização do conteúdo de um Viewport.

- Configure em `WorldEnvironment` → aplica a todos os Viewports.
- Configure em `Camera3D` → aplica apenas ao Viewport usando aquela câmera.
- Crie o resource `Compositor` no node desejado e adicione `CompositorEffect`s a ele.

> ⚠ Evite: usar o Compositor no renderer **Compatibility** — suportado apenas por **Mobile** e **Forward+**.

### 39.2 CompositorEffect — Implementação

`CompositorEffect` insere lógica customizada no pipeline de renderização em estágios definidos. O callback roda na **thread de renderização** — use `Mutex` para acesso a dados compartilhados.

**Estrutura mínima:**

```gdscript
@tool
extends CompositorEffect
class_name PostProcessShader

var rd: RenderingDevice
var shader: RID
var pipeline: RID
var mutex: Mutex = Mutex.new()
var shader_is_dirty: bool = true

@export_multiline var shader_code: String = "":
    set(value):
        mutex.lock()
        shader_code = value
        shader_is_dirty = true
        mutex.unlock()

func _init():
    effect_callback_type = EFFECT_CALLBACK_TYPE_POST_TRANSPARENT
    rd = RenderingServer.get_rendering_device()

func _notification(what):
    if what == NOTIFICATION_PREDELETE:
        if shader.is_valid():
            rd.free_rid(shader)   # pipeline dependente é liberado automaticamente

func _render_callback(p_effect_callback_type, p_render_data):
    if rd and p_effect_callback_type == EFFECT_CALLBACK_TYPE_POST_TRANSPARENT and _check_shader():
        var render_scene_buffers: RenderSceneBuffersRD = p_render_data.get_render_scene_buffers()
        if render_scene_buffers:
            var size = render_scene_buffers.get_internal_size()
            if size.x == 0 and size.y == 0:
                return
            var x_groups = (size.x - 1) / 8 + 1
            var y_groups = (size.y - 1) / 8 + 1
            # Push constant: PackedFloat32Array com alinhamento de 16 bytes (múltiplo de 4 elementos)
            var push_constant: PackedFloat32Array = PackedFloat32Array([size.x, size.y, 0.0, 0.0])
            for view in range(render_scene_buffers.get_view_count()):
                var input_image = render_scene_buffers.get_color_layer(view)
                var uniform: RDUniform = RDUniform.new()
                uniform.uniform_type = RenderingDevice.UNIFORM_TYPE_IMAGE
                uniform.binding = 0
                uniform.add_id(input_image)
                # UniformSetCacheRD evita vazamento de memória com uniform sets por frame
                var uniform_set = UniformSetCacheRD.get_cache(shader, 0, [uniform])
                var compute_list := rd.compute_list_begin()
                rd.compute_list_bind_compute_pipeline(compute_list, pipeline)
                rd.compute_list_bind_uniform_set(compute_list, uniform_set, 0)
                rd.compute_list_set_push_constant(compute_list, push_constant.to_byte_array(), push_constant.size() * 4)
                rd.compute_list_dispatch(compute_list, x_groups, y_groups, 1)
                rd.compute_list_end()
```

**Compilação do compute shader em runtime:**

```gdscript
func _check_shader() -> bool:
    if not rd: return false
    var new_code: String = ""
    mutex.lock()
    if shader_is_dirty:
        new_code = shader_code
        shader_is_dirty = false
    mutex.unlock()
    if new_code.is_empty(): return pipeline.is_valid()
    if shader.is_valid():
        rd.free_rid(shader)
        shader = RID(); pipeline = RID()
    var src := RDShaderSource.new()
    src.language = RenderingDevice.SHADER_LANGUAGE_GLSL
    src.source_compute = template_shader.replace("#COMPUTE_CODE", new_code)
    var spirv := rd.shader_compile_spirv_from_source(src)
    if spirv.compile_error_compute != "":
        push_error(spirv.compile_error_compute); return false
    shader = rd.shader_create_from_spirv(spirv)
    if not shader.is_valid(): return false
    pipeline = rd.compute_pipeline_create(shader)
    return pipeline.is_valid()
```

**Regras:**
- O `effect_callback_type` só dá acesso ao pipeline 3D — nenhum estágio 2D disponível atualmente.
- Use `UniformSetCacheRD` em vez de criar uniform sets manualmente — o cache os libera automaticamente quando os buffers mudam.
- Compilação em runtime é ótima para protótipos, mas impede pré-compilação/cache (problema em consoles). Para produção, use um arquivo `.glsl` completo (o engine consegue pré-compilar e cachear).
- O loop por views é necessário para renderização estéreo (XR); em mono há apenas uma view, sem custo extra.

**Adicionar ao compositor no editor:** Compositor → expandir `compositor_effects` → Add Element → selecionar a classe do efeito.

### 39.3 Custom Post-Processing (Canvas Layer)

Abordagem mais simples usando a pipeline de canvas (sem compute shaders, apenas 3D indisponível).

**Single-pass:**
1. Adicione `CanvasLayer` → filho `ColorRect` → `ShaderMaterial` novo.
2. Defina o anchor preset do `ColorRect` como **Full Rect**.
3. No shader, acesse o frame atual:

```gdshader
shader_type canvas_item;
uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

void fragment() {
    COLOR = textureLod(screen_texture, SCREEN_UV, 0.0);
    // modifique COLOR aqui
}
```

**Multi-pass:** Empilhe múltiplos `CanvasLayer + ColorRect`. Cada layer superior recebe o resultado do inferior como `screen_texture`. Exemplo: blur Gaussiano separado em passe X e passe Y em dois CanvasLayers distintos.

**Regra**: Use `BackBufferCopy` para capturar apenas uma região da tela — mais eficiente que capturar o frame inteiro quando o efeito afeta área limitada.

> ⚠ Evite: Esperar acesso a buffers de profundidade (depth), normais ou roughness via `hint_screen_texture` — apenas o frame renderizado e buffers explicitamente expostos pelo Godot estão disponíveis.

---

## 40. XR / Realidade Virtual e Aumentada

### 40.1 Visão Geral — Sistema XR

- **XRServer** — singleton central; descobre e gerencia interfaces XR.
- **XRInterface** — implementação por plataforma; registra-se no XRServer automaticamente.
- **Renderer recomendado**: `Mobile` para desktop VR; `Compatibility (OpenGL)` para headsets standalone (Quest).
  - `Forward+` funciona mas não está otimizado para XR atualmente.
- **Apenas uma interface primária** pode gerenciar saída para HMD ao mesmo tempo.

**Nodes XR essenciais:**

| Node | Propósito |
|------|-----------|
| `XROrigin3D` | Centro do tracking space; todos os nodes rastreados são filhos dele |
| `XRCamera3D` | Câmera estéreo; posicionada automaticamente pelo sistema XR |
| `XRController3D` | Controle (mão esq/dir); emite signals de botões/poses; posicionado pelo XR |

> ⚠ Evite: Chamar `initialize()` múltiplas vezes ao trocar de cena — inicialize apenas uma vez e carregue levels como subscenas.

### 40.2 Setup da Cena XR

**Estrutura mínima:**
```
Node3D (root)  ← script de inicialização
├── XROrigin3D
│   ├── XRCamera3D
│   ├── XRController3D "LeftHand"   tracker=/user/hand/left   pose=aim
│   └── XRController3D "RightHand"  tracker=/user/hand/right  pose=aim
├── DirectionalLight3D
└── WorldEnvironment
```

**Script mínimo:**
```gdscript
extends Node3D

func _ready():
    var xr_interface = XRServer.find_interface("OpenXR")
    if xr_interface and xr_interface.is_initialized():
        DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED)
        get_viewport().use_xr = true
    else:
        print("OpenXR not initialized, headset connected?")
```

**Posições de desenvolvimento** (para preview no editor): câmera y=1.7; controllers em ±0.5, 1.0, -0.5.

**OpenXR deve ser habilitado** em Project Settings → XR → OpenXR → Enabled (obrigatório para Vulkan/antes do boot).
Também habilite: XR → Shaders → Enabled → Save & Restart.

### 40.3 Script de Inicialização XR (Completo)

Script para o root node. Gerencia ciclo de vida da sessão OpenXR, refresh rate e foco.

```gdscript
extends Node3D

signal focus_lost
signal focus_gained
signal pose_recentered

@export var maximum_refresh_rate: int = 90

var xr_interface: OpenXRInterface
var xr_is_focussed := false

func _ready():
    xr_interface = XRServer.find_interface("OpenXR")
    if xr_interface and xr_interface.is_initialized():
        var vp := get_viewport()
        vp.use_xr = true
        DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED)
        # Foveated rendering
        if RenderingServer.get_rendering_device():
            vp.vrs_mode = Viewport.VRS_XR  # Mobile / Forward+
        elif int(ProjectSettings.get_setting("xr/openxr/foveation_level")) == 0:
            push_warning("Recomenda-se Foveation Level High (Compatibility renderer)")
        # Sinais de sessão
        xr_interface.session_begun.connect(_on_openxr_session_begun)
        xr_interface.session_visible.connect(_on_openxr_visible_state)
        xr_interface.session_focussed.connect(_on_openxr_focused_state)
        xr_interface.session_stopping.connect(_on_openxr_stopping)
        xr_interface.pose_recentered.connect(_on_openxr_pose_recentered)
    else:
        get_tree().quit()  # app VR-only: sair se sem headset

func _on_openxr_session_begun() -> void:
    # Acertar refresh rate mais alto disponível dentro do limite configurado
    var cur = xr_interface.get_display_refresh_rate()
    var best = cur
    for rate in xr_interface.get_available_display_refresh_rates():
        if rate > best and rate <= maximum_refresh_rate:
            best = rate
    if cur != best:
        xr_interface.set_display_refresh_rate(best)
        cur = best
    Engine.physics_ticks_per_second = cur  # eliminar stuttering físico

func _on_openxr_visible_state() -> void:
    # Headset tirado / menu do sistema aberto
    if xr_is_focussed:
        xr_is_focussed = false
        get_tree().paused = true
        emit_signal("focus_lost")

func _on_openxr_focused_state() -> void:
    xr_is_focussed = true
    get_tree().paused = false
    emit_signal("focus_gained")

func _on_openxr_stopping() -> void:
    pass  # sessão encerrando (plataforma-dependente)

func _on_openxr_pose_recentered() -> void:
    emit_signal("pose_recentered")
    # Recentrar: XRServer.center_on_hmd(XRServer.RESET_BUT_KEEP_TILT, true)
```

**Regras:**
- **Pausar no visible state** é obrigatório — controller/hand tracking é desabilitado no estado visible; não fazer isso pode causar comportamento inesperado ao retornar.
- **`Engine.physics_ticks_per_second` deve coincidir com o refresh rate** do headset (mínimo 72Hz) — física a 60Hz em headset 90Hz gera stuttering visível.
- **VSync desativado** — OpenXR faz sync próprio; VSync ativo limita FPS ao monitor.

### 40.4 OpenXR — Configurações

*Project Settings → XR → OpenXR*

**Form Factor:** `Head Mounted` (Quest, Index) ou `Handheld` (telefone AR). OpenXR falha ao inicializar se não bater com o hardware.

**View Configuration:** `Stereo` (headsets) ou `Mono` (telefone AR). Idem.

**Reference Space** — onde fica o `XROrigin3D` em relação ao espaço físico:

| Espaço | Origem | Melhor para | Observação |
|--------|--------|-------------|------------|
| `Local` | Cabeça do jogador | Simuladores (voo, corrida) | Não use `center_on_hmd` |
| `Stage` (padrão) | Centro do play space (guardian) | Room scale | Recentrar: `XRServer.center_on_hmd(RESET_BUT_KEEP_TILT, false/true)` |
| `Local Floor` | Como Local, mas mantém altura | Jogos em pé estacionários | Cuidado com movimento virtual + recenter |

**Foveated rendering:**
- Compatibility: configurar `xr/openxr/foveation_level` (Low–High) + `foveation_dynamic`.
- Mobile/Forward+: `viewport.vrs_mode = Viewport.VRS_XR`.

**Extensions úteis (ativar em Project Settings → XR → OpenXR → Extensions):**

| Extension | Para que serve |
|-----------|---------------|
| Hand Tracking | Rastreamento óptico de mãos |
| Hand Interaction Profile | Gestos (pinch/grasp/poke) via action map |
| Eye Gaze Interaction | Rastreamento ocular (`/user/eyes_ext`) |
| Render Models | Modelos 3D dos controllers fornecidos pelo runtime |
| Frame Synthesis | Motion vectors para reprojection (não funciona no Forward+) |
| Analog Threshold | Threshold customizado para inputs analógicos |
| Dpad Binding | Converte thumbstick em 4 botões |

### 40.5 Action Map XR

*Project → XR Action Map (requer OpenXR habilitado)*

Ações nomeadas + bindings por perfil de controller → runtime faz a correspondência de hardware.

**Tipos de ação:**

| Tipo | Uso | GDScript |
|------|-----|---------|
| `Bool` | Botões digitais | `is_button_pressed("action")` / signal `button_pressed` |
| `Float` | Triggers, grips analógicos | `get_float("action")` / signal `input_float_changed` |
| `Vector2` | Thumbstick, trackpad | `get_vector2("action")` / signal `input_vector2_changed` |
| `Pose` | Posição/orientação rastreada (`aim`, `grip`, `palm`) | posiciona o `XRController3D` automaticamente |
| `Haptic` | Vibração (output) | `trigger_haptic_pulse("haptic", freq, amp, dur, delay)` |

**Action Sets:** Agrupe ações por estado do jogo (Character, Vehicle, Menu). Ative/desative por set; prioridade numérica resolve conflitos.

> ⚠ Evite: Usar `Bool` para triggers/grips — runtimes aplicam thresholds inconsistentes. Prefira `Float` e aplique threshold manual no código.

**Profiles:** Configure apenas controllers que você testou. O runtime faz fallback para o Touch controller da Meta (base para a maioria dos runtimes). Evite adivinhar bindings para hardware não testado — o runtime faz um trabalho melhor de rebinding.

**Binding Modifiers (requerem ativação em Project Settings):**
- `Dpad Binding`: converte thumbstick/trackpad em 4 inputs separados (up/down/left/right).
- `Analog Threshold`: define on-threshold e off-threshold para actions Bool em inputs analógicos.

### 40.6 AR / Passthrough

**Environment Blend Mode** — via `xr_interface.environment_blend_mode`:

| Modo | Resultado | Configuração extra |
|------|-----------|--------------------|
| `XR_ENV_BLEND_MODE_OPAQUE` | VR puro (mundo real invisível) | — |
| `XR_ENV_BLEND_MODE_ADDITIVE` | Renderizado adicionado ao mundo real (see-through) | Fundo do sky = preto |
| `XR_ENV_BLEND_MODE_ALPHA_BLEND` | Blend com alpha (passthrough Quest/HTC) | `viewport.transparent_bg = true` |

```gdscript
func switch_to_ar() -> bool:
    var xr_interface := XRServer.primary_interface
    if not xr_interface: return false
    var modes = xr_interface.get_supported_environment_blend_modes()
    if XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND in modes:
        xr_interface.environment_blend_mode = XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND
        get_viewport().transparent_bg = true
    elif XRInterface.XR_ENV_BLEND_MODE_ADDITIVE in modes:
        xr_interface.environment_blend_mode = XRInterface.XR_ENV_BLEND_MODE_ADDITIVE
        get_viewport().transparent_bg = false
    else:
        return false
    # Fundo transparente não contribui para iluminação — ajuste:
    $WorldEnvironment.environment.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
    return true
```

**Shadow to opacity** — shader espacial para AR: superfície fica opaca em sombra, transparente quando iluminada:
```gdshader
shader_type spatial;
render_mode blend_mix, depth_draw_opaque, cull_back, shadow_to_opacity;
void fragment() { ALBEDO = vec3(0.0, 0.0, 0.0); }
```
Casos de uso: mesh da mão do usuário que oclui objetos virtuais; plano invisible sobre mesa real que recebe sombras de objetos virtuais.

### 40.7 Room Scale — Movimento com Física

**Dois problemas fundamentais** ao combinar roomscale + movimento virtual:
1. Rotação via joystick move o jogador em arco em vez de no lugar.
2. `CharacterBody3D` não sabe onde o jogador está — `XRCamera3D` é a posição real.

**Solução 1 — Origin-Centric** (`CharacterBody3D` com `top_level = true`):

```gdscript
# Passo 1: Mover CharacterBody para onde o jogador está fisicamente
func _process_on_physical_movement(delta) -> bool:
    var cur_vel = $CharacterBody3D.velocity
    var org = $CharacterBody3D.global_transform.origin
    var dest = global_transform * ($XRCamera3D.transform * $XRCamera3D/Neck.transform.origin)
    dest.y = 0.0
    $CharacterBody3D.velocity = (dest - org) / delta
    $CharacterBody3D.move_and_slide()
    $CharacterBody3D.velocity = cur_vel
    var left = (dest - $CharacterBody3D.global_transform.origin)
    left.y = 0.0
    return left.length() > 0.01  # true = colidiu

# Passo 2: Rotacionar XROrigin3D em torno do jogador (não do centro do tracking space)
func _process_rotation_on_input(delta):
    var player_pos = $CharacterBody3D.global_transform.origin - global_transform.origin
    var t1 = Transform3D(); t1.origin = -player_pos
    var t2 = Transform3D(); t2.origin = player_pos
    var rot = Transform3D().rotated(Vector3.UP, _get_rotational_input() * delta)
    global_transform = (global_transform * t2 * rot * t1).orthonormalized()

# Passo 3: Movimento por input — aplicar delta ao XROrigin3D
func _process_movement_on_input(delta):
    var org = $CharacterBody3D.global_transform.origin
    var input = _get_movement_input()  # Vector2 em m/s
    $CharacterBody3D.velocity.y -= gravity * delta
    $CharacterBody3D.velocity.x = ($CharacterBody3D.global_transform.basis * Vector3(input.x, 0, input.y)).x
    $CharacterBody3D.velocity.z = ($CharacterBody3D.global_transform.basis * Vector3(input.x, 0, input.y)).z
    $CharacterBody3D.move_and_slide()
    global_transform.origin += $CharacterBody3D.global_transform.origin - org
```

**Solução 2 — Character-Centric** (`CharacterBody3D` como root — mais parecido com FPS padrão):

Passo 1: Rotacionar `CharacterBody` para alinhar com a câmera, reverter no `XROrigin3D`, mover `CharacterBody` e mover `XROrigin3D` de volta pelo delta.
Passo 2/3: Rotação e movimento via input — implementar como FPS normal.

**Quando o jogador anda para onde não pode:**
Não tente bloquear o movimento físico — causa náusea. Em vez disso:
1. Meça distância entre posição virtual do CharacterBody e posição física da câmera.
2. Acima de alguns centímetros, escureça a tela gradualmente (fade to black).

**Regras:**
- Comece testando em pé e andando o quanto antes — problemas de roomscale só surgem nesse contexto.
- Implemente snap turn (padrão) ou smooth turn com vignette — sem opção de conforto haverá náusea.
- Use a altura da câmera para adaptar a collision shape (agachado/em pé/deitado).
- Na carga inicial da cena, mova o XROrigin para que o jogador inicie na posição correta.

### 40.8 Composition Layers (UI 2D em XR)

**Problema:** UI 2D renderizada normalmente perde qualidade por lens distortion do runtime XR.

**Solução:** Nodes `OpenXRCompositionLayerQuad/Cylinder/Equirect` — o runtime composita o SubViewport *após* a distortion, resultando em texto nitido no headset.

**Estrutura:**
```
XROrigin3D
└── OpenXRCompositionLayerQuad   ← posicionar ~1-1.5m do jogador, na altura dos olhos
    └── SubViewport              ← UI 2D aqui dentro (transparent = true)
```

**Pointer via raycast do controller:**
```gdscript
extends OpenXRCompositionLayerQuad

const NO_INTERSECTION = Vector2(-1.0, -1.0)
@export var controller: XRController3D
@export var button_action := "trigger_click"

var was_pressed := false
var was_intersect := NO_INTERSECTION

func _process(_delta):
    if not (controller and layer_viewport): return
    var ct := controller.global_transform
    var intersect := intersects_ray(ct.origin, -ct.basis.z)

    if intersect != NO_INTERSECTION:
        var is_pressed := controller.is_button_pressed(button_action)
        var vp_pos := Vector2i(intersect * Vector2(layer_viewport.size))

        if was_intersect != NO_INTERSECTION and intersect != was_intersect:
            var ev := InputEventMouseMotion.new()
            ev.position = vp_pos
            ev.relative = vp_pos - Vector2i(was_intersect * Vector2(layer_viewport.size))
            if was_pressed: ev.button_mask = MOUSE_BUTTON_MASK_LEFT
            layer_viewport.push_input(ev)

        if not is_pressed and was_pressed:
            var ev := InputEventMouseButton.new()
            ev.button_index = 1; ev.pressed = false; ev.position = vp_pos
            layer_viewport.push_input(ev)
        elif is_pressed and not was_pressed:
            var ev := InputEventMouseButton.new()
            ev.button_index = 1; ev.button_mask = MOUSE_BUTTON_MASK_LEFT
            ev.pressed = true; ev.position = vp_pos
            layer_viewport.push_input(ev)

        was_pressed = is_pressed
        was_intersect = intersect
    else:
        was_pressed = false; was_intersect = NO_INTERSECTION
```

**Hole Punch:** Habilitar quando objetos virtuais devem aparecer *à frente* da UI — Godot renderiza a área transparente para que a composição do runtime fique correta. Requer `Sort Order` negativo.

> ⚠ Aviso: Composition layers **não aparecem na janela espectador** (desktop) — apenas no headset.

### 40.9 Hand Tracking

**Habilitando:** Project Settings → XR → OpenXR → Extensions → Hand Tracking: On.
Para Meta Quest: também habilitar na export preset.

**Estrutura por mão:**
```
XROrigin3D
└── XRNode3D   tracker=/user/hand_tracker/left   pose=default   show_when_tracked=true
    └── [glTF rigged hand mesh]
        └── Skeleton3D
            └── XRHandModifier3D   Hand Tracker=/user/hand_tracker/left
```

**Bone Update Mode no XRHandModifier3D:**
- `Full` — aplica tamanho real da mão; pode deformar mesh se não ponderada corretamente para variações de tamanho.
- `Rotation Only` — mantém comprimento dos ossos do mesh; mais seguro para modelos genéricos.

**Detectar fonte do tracking:**
```gdscript
var ht: XRHandTracker = XRServer.get_tracker("/user/hand_tracker/left")
if ht and ht.has_tracking_data:
    match ht.hand_tracking_source:
        XRHandTracker.HAND_TRACKING_SOURCE_UNOBSTRUCTED:
            pass  # câmeras do headset rastreando opticamente
        XRHandTracker.HAND_TRACKING_SOURCE_CONTROLLER:
            pass  # inferido da posição/inputs do controller
        XRHandTracker.HAND_TRACKING_SOURCE_UNKNOWN:
            pass  # runtime não informa — fazer inferência pela plataforma
```

**Interaction Profiles para gestos no action map:**

| Profile | Gestos | Trackers usados |
|---------|--------|-----------------|
| Hand Interaction Profile | pinch, grasp, poke | `/user/hand/left|right` (unificado com controller) |
| Microsoft Hand Interaction | select (pinch), squeeze (grasp) | `/user/hand/left|right` |
| Simple Controller (fallback) | varia por runtime (ex.: pinch = select click) | `/user/hand/left|right` |

> ⚠ Se nenhum profile de hand interaction for suportado, implemente detecção de gestos própria via `XRHandTracker` (joint positions/rotations de todos os ossos dos dedos).

### 40.10 Body Tracking e Render Models

**Body Tracking (HTC Trackers via SteamVR ou HTC Elite XR):**
Adicione `XRController3D` como filhos do `XROrigin3D` com tracker paths por papel:
`/user/vive_tracker_htcx/role/left_foot`, `/role/right_foot`, `/role/waist`, `/role/chest`, `/role/left_elbow`, `/role/right_elbow`, etc.
Use esses nodes como IK targets para um avatar de corpo inteiro.

**Render Models (OpenXR Render Models API):**
Mostra o modelo 3D correto do controller para o hardware real do usuário, fornecido pelo runtime (sem adivinhar qual controller está sendo usado).

**Setup com `OpenXRRenderModelManager`:**
```
XROrigin3D
├── OpenXRRenderModelManager   target=None set       ← tudo sem mão associada
├── XRController3D "LeftHand"
│   ├── AnimatableBody3D (collision hands)
│   └── OpenXRRenderModelManager  target=Left Hand  make_local_to_pose=grip_pose
└── XRController3D "RightHand"
    ├── AnimatableBody3D (collision hands)
    └── OpenXRRenderModelManager  target=Right Hand  make_local_to_pose=grip_pose
```

**CollisionHands (impede mão de atravessar paredes):**
```gdscript
class_name CollisionHands3D
extends AnimatableBody3D

func _ready():
    top_level = true
    sync_to_physics = false
    process_physics_priority = -90  # rodar após movimento do XROrigin

func _physics_process(_delta):
    var dest := get_parent().global_transform
    global_basis = dest.basis
    move_and_collide(dest.origin - global_position)
```

Habilitar em Project Settings → XR → OpenXR → Extensions → Render Models.

### 40.11 XR Fullscreen Effects

Para efeitos de tela cheia centrados no olhar do usuário (ex.: vignette), compensar o **FOV assimétrico** do HMD:

```gdshader
shader_type spatial;
render_mode depth_test_disabled, skip_vertex_transform, unshaded, cull_disabled;

void vertex() {
    vec2 vert_pos = VERTEX.xy;
    if (length(vert_pos) < 0.99) {
        vec4 offset = PROJECTION_MATRIX * vec4(0.0, 0.0, 1.0, 1.0);
        vert_pos += (offset.xy / offset.w);
    }
    POSITION = vec4(vert_pos, 1.0, 1.0);
}

void fragment() {
    ALBEDO = vec3(0.0);
    ALPHA = dot(UV * 2.0 - 1.0, UV * 2.0 - 1.0) * 2.0;
}
```

**Setup:** `MeshInstance3D` filho do `XRCamera3D` com `QuadMesh` (size 2×2, subdivisions ≥2) e este shader.

> ⚠ Evite: Ler `screen_texture` em efeitos de tela cheia no XR — desabilita todas as otimizações de renderização estéreo (cópia completa do render buffer por frame).

### 40.12 Deploy Android e XR Tools

**Deploy Android (headsets standalone como Meta Quest):**
1. Configurar export Android padrão (OpenJDK 17, Android Studio, SDK).
2. Project → Install Android Build Template.
3. Asset Library → buscar "OpenXR vendors" → instalar plugin (v3+ necessário para passthrough).
4. Criar export preset por device: Android → Use Gradle Build → XR Mode = OpenXR → selecionar vendor plugin.
5. A partir do Godot 4.6, o vendor plugin é opcional (APK universal) mas recomendado para app stores.

> ⚠ Use Compatibility (OpenGL) para headsets Android — Mobile Vulkan ainda está em polimento.

**Godot XR Tools** (`https://github.com/GodotVR/godot-xr-tools`) — toolkit para OpenXR/WebXR:

| Componente | Caminho | O que faz |
|-----------|---------|-----------|
| `PlayerBody` | `addons/godot-xr-tools/player/player_body.tscn` | Gravidade, física e colisão do jogador (filho do XROrigin3D) |
| `MovementDirect` | `.../functions/movement_direct.tscn` | Movimento via joystick (frente/trás + strafe opcional) |
| `MovementTurn` | `.../functions/movement_turn.tscn` | Rotação snap (padrão) ou smooth |
| `FunctionTeleport` | `.../functions/function_teleport.tscn` | Teleporte: pressionar trigger, apontar, soltar |
| Mãos low poly | `.../hands/lowpoly/left_hand_low.tscn` | Mãos animadas por trigger/grip |
| Mãos high poly | `.../hands/highpoly/left_hand_high.tscn` | Alta qualidade (evitar em mobile) |

Adicione `PlayerBody` ao `XROrigin3D`, depois adicione `MovementDirect` + `MovementTurn` ao `XRController3D` da mão direita e `FunctionTeleport` à mão esquerda.

---

## 41. Engine Architecture

### 41.1 Visão Geral da Arquitetura

A arquitetura do Godot é organizada em camadas, da mais alta para a mais baixa:

| Camada | Diretório fonte | Responsabilidade |
|--------|----------------|-----------------|
| **Scene Layer** | `/scene/*` | Sistema de cena, SceneTree, Node — a interface principal para construir jogos |
| **Server Layer** | `/servers/*` | Subsistemas como RenderingServer, AudioServer, PhysicsServer — singletons inicializados no startup |
| **Drivers / Platform** | `/drivers/*`, `/platform/*` | Abstrações de hardware: backends gráficos (Vulkan, OpenGL), áudio, OS, DisplayServer |
| **Core** | `/core/*` | Object, ClassDB, gerenciamento de memória, containers, Variant, I/O |
| **Main** | `/main/*` | Inicialização, shutdown e MainLoop do engine |

**Regra:** Prefira usar APIs da Scene Layer em GDScript. Acesse Servers diretamente apenas quando precisar de operações de baixo nível não expostas por Node (ex.: criar malhas proceduralmente via `RenderingServer`).

> ⚠ Evite: Chamar métodos de servidor (RenderingServer, PhysicsServer) de threads arbitrárias — eles não são thread-safe; use chamadas diferidas ou o thread principal.

---

### 41.2 Métodos e Macros Comuns (C++)

Esta seção é relevante para quem desenvolve módulos C++ ou contribui com o engine.

#### Print e saída

```cpp
// Imprime na saída padrão (concatena automaticamente com espaço)
print_line("Mensagem");
print_line("Há", 123, "nodes");

// Só imprime com --verbose
print_verbose("Detalhe interno");

// Com BBCode (visível no painel Output do editor)
print_line_rich("[b]Negrito[/b], [color=red]vermelho[/color]");

// Erro / aviso com trace
ERR_PRINT("Mensagem de erro");
WARN_PRINT("Aviso");

// Erro/aviso apenas uma vez por sessão (evita spam)
ERR_PRINT_ONCE("Erro único");
WARN_PRINT_ONCE("Aviso único");
```

#### Format strings

```cpp
// Equivalente ao sprintf do C — use em vez de concatenação
vformat("Meu nome é %s.", "Godette");
vformat("%d bugs na parede!", 1234);
vformat("Pi ≈ %f.", 3.1416);

// Converter resultado para const char*
vformat("Arquivo: %s", path).utf8().get_data();
```

**Regra:** Prefira `vformat()` a concatenação de strings — é mais legível e mais eficiente.

#### Conversão int/float para String

```cpp
String s_int  = itos(42);       // "42"
String s_real = rtos(123.45);   // "123.45"
```

#### Internacionalização (i18n)

```cpp
// TTR() — traduções do editor (não afeta projetos do usuário)
TTR("Sair do editor?");

// RTR() — traduções de runtime (localizadas em projetos)
// (usar somente fora de código exclusivo do editor)

// Combinação correta com placeholder:
String caminho = "arquivo.txt";
vformat(TTR("Não foi possível abrir \"%s\" para leitura."), caminho);
// ERRADO: TTR(vformat(...)) — a string não bate com traduções
```

> ⚠ Evite: Envolver `vformat()` dentro de `TTR()` — o placeholder já estará substituído antes de chegar ao TranslationServer.

#### Clamp de valores

```cpp
int a = 3, b = 5;
MAX(b, 6);          // 6
MIN(2, a);          // 2
CLAMP(a, 10, 30);   // 10
```

#### Microbenchmarking

```cpp
#include "core/os/time.h"
uint64_t inicio = Time::get_singleton()->get_ticks_usec();
// ... código a medir ...
uint64_t fim = Time::get_singleton()->get_ticks_usec();
print_line(vformat("Trecho levou %d microssegundos", fim - inicio));
```

**Regra:** Remova snippets de benchmark antes de abrir Pull Request.

#### Project/Editor settings

```cpp
// Define e retorna (primeira vez — especifica default)
GLOBAL_DEF("section/subsection/valor", false);
EDITOR_DEF("section/subsection/valor", "Sem título");

// Acessa sem redefinir (demais locais)
GLOBAL_GET("section/subsection/valor");
EDITOR_GET("section/subsection/valor");
```

**Regra:** Use `GLOBAL_DEF`/`EDITOR_DEF` apenas uma vez por configuração; use `GLOBAL_GET`/`EDITOR_GET` em todos os outros pontos.

#### Macros de erro

> ⚠ Atenção: nas macros de erro do Godot, a condição dispara o erro quando é **verdadeira** (inverso de `assert()`).

```cpp
// Retorna void se condição for verdadeira
ERR_FAIL_COND_MSG(!mesh.is_valid(),
    vformat("Não foi possível carregar mesh em: %s", path));

// Retorna valor se condição for verdadeira
ERR_FAIL_COND_V_MSG(rect.x < 0 || rect.y < 0, 0,
    "Não foi possível calcular a área do retângulo.");

// Verifica índice fora de range (0 .. MAX-1), retorna void
ERR_FAIL_INDEX_MSG(index, SomeEnum::QUALITY_MAX,
    vformat("Qualidade inválida: %d.", index));

// Verifica índice fora de range, retorna valor
ERR_FAIL_INDEX_V_MSG(index, some_array.size(), -1,
    vformat("Item %d fora dos limites.", index));

// Erro incondicional
ERR_FAIL_MSG("Não foi possível recarregar o cache.");
ERR_FAIL_V_MSG(false, "Não foi possível analisar os argumentos.");

// Crash (raramente usado — Godot nunca deve crashar em produção)
CRASH_NOW_MSG("Estado impossível atingido.");
```

---

### 41.3 Core Types

#### Gerenciamento de memória

```cpp
// C-style
void* p = memalloc(size);
p = memrealloc(p, novo_size);
memfree(p);

// C++-style (chama _init/_finalize automáticos)
MyClass* obj = memnew(MyClass);
memnew(MyClass(arg1, arg2));
memdelete(obj);

MyClass* arr = memnew_arr(MyClass, 10);
memdelete_arr(arr);
```

**Regra:** Nunca use `new`/`delete` direto no codebase do Godot — use `memnew`/`memdelete` para garantir rastreamento de memória e notificações automáticas.

#### Containers

| Tipo Godot | Equivalente STL | Quando usar |
|-----------|----------------|-------------|
| `String` | `std::string` | String padrão (UTF-32, tamanho fixo por char) |
| `Vector<T>` | `std::vector` | Vetor padrão com COW (copy-on-write) |
| `LocalVector<T>` | `std::vector` | Quando COW não é necessário e performance importa |
| `AHashMap<K,V>` | `std::unordered_map` | Mapa padrão (não preserva ordem de inserção) |
| `HashMap<K,V>` | `std::unordered_map` | Quando ponteiros/iteradores precisam ser estáveis sob mutação |
| `HashSet<T>` | `std::unordered_set` | Conjunto padrão |
| `StringName` | `std::string` | Strings estáticas frequentes (interning para comparação O(1)) |
| `Array` | `std::vector` | Array de Variant (sem tipagem estática, refcount compartilhado) |
| `TypedArray<T>` | `std::vector` | Array com tipagem estática de elementos |
| `Packed*Array` | `std::vector` | Alias de `Vector<T>`: PackedColorArray, PackedVector3Array, etc. |
| `Dictionary` | `std::unordered_map` | Chaves/valores Variant, preserva ordem de inserção |
| `TypedDictionary<K,V>` | `std::unordered_map` | Dictionary com tipagem estática |
| `FixedVector<T,N>` | `std::array` | Capacidade fixa, sem alocação heap |
| `Span<T>` | `std::span` | Acesso read-only a array contíguo sem copiar |
| `List<T>` | `std::list` | Lista encadeada (preferir outros em código novo) |

**Regra:** Containers do Godot assumem que os elementos são *trivially relocatable*. Não armazene tipos que tenham ponteiros para si mesmos como elementos.

> ⚠ Evite: Usar containers da STL (`std::vector`, `std::string`) no codebase do engine — use os tipos Godot.

#### Multithreading / Concorrência

Nenhum container do Godot é thread-safe. Use proteções explícitas:

| Tipo | Equivalente STL | Uso |
|------|----------------|-----|
| `Mutex` | `std::recursive_mutex` | Mutex recursivo; `MutexLock lock(m)` |
| `BinaryMutex` | `std::mutex` | Mutex não recursivo |
| `RWLock` | `std::shared_timed_mutex` | Leitura/escrita: `RWLockRead r(m)` / `RWLockWrite w(m)` |
| `SafeBinaryMutex` | `std::mutex` | Mutex recursivo para uso com `ConditionVariable` |
| `ConditionVariable` | `std::condition_variable` | Variável de condição |
| `Semaphore` | `std::counting_semaphore` | Semáforo contador |
| `SafeNumeric<T>` | `std::atomic` | Atômico numérico |
| `SafeFlag` | `std::atomic_bool` | Flag booleana atômica |
| `SafeRefCount` | `std::atomic` | Contagem de referência — recusa incrementar se for 0 |

#### Math types

Tipos matemáticos disponíveis em `/core/math/`:
`Vector2`, `Vector2i`, `Vector3`, `Vector3i`, `Vector4`, `Vector4i`, `Rect2`, `Rect2i`, `AABB`, `Plane`, `Quaternion`, `Basis`, `Transform2D`, `Transform3D`, `Projection`, `Color`

#### NodePath

Tipo especial para armazenar caminhos na árvore de cena e referenciá-los de forma otimizada (`core/string/node_path.h`).

```gdscript
# GDScript
var caminho: NodePath = NodePath("../../Player/Sprite2D")
get_node(caminho)
```

#### RID (Resource ID)

RIDs são identificadores opacos usados pelos Servers para referenciar dados internos. Não permitem acesso direto aos dados. São únicos mesmo entre tipos diferentes.

```gdscript
# GDScript — criar mesh via RenderingServer (baixo nível)
var rid: RID = RenderingServer.mesh_create()
# usar rid em chamadas subsequentes de RenderingServer
RenderingServer.free_rid(rid)
```

---

### 41.4 Variant

`Variant` é o tipo de dado mais importante do Godot — usado para comunicação, serialização, propriedades e chamadas de métodos. Ocupa 24 bytes em plataformas 64-bit.

**Capacidades da Variant:**
- Armazena quase qualquer tipo do engine
- Realiza operações entre variants (base do GDScript)
- Hash para comparação rápida
- Conversão segura entre tipos
- Abstração de chamadas de métodos com argumentos
- Serialização binária (disco/rede) e textual
- Deferral de chamadas e passagem de dados entre threads

**Nota:** Todos os tipos dentro de Variant exceto `Nil` e `Object` são **não-nulos** (non-nullable) — sempre contêm um valor válido.

#### Tipos suportados pela Variant

| Tipo | Observação |
|------|-----------|
| `Nil` | Nullable — único tipo que pode ser `null` |
| `bool`, `int`, `float` | Primitivos |
| `String`, `StringName`, `NodePath` | Strings |
| `Vector2`, `Vector2i`, `Vector3`, `Vector3i`, `Vector4`, `Vector4i` | Vetores |
| `Rect2`, `Rect2i`, `AABB` | Retângulos/caixas |
| `Transform2D`, `Transform3D`, `Basis`, `Projection` | Transformações |
| `Plane`, `Quaternion`, `Color` | Matemática e cor |
| `RID` | Resource ID opaco |
| `Object` | Nullable |
| `Callable`, `Signal` | Chamáveis e sinais |
| `Dictionary`, `Array` | Containers dinâmicos |
| `PackedByteArray`, `PackedInt32Array`, `PackedInt64Array` | Arrays empacotados |
| `PackedFloat32Array`, `PackedFloat64Array` | Arrays empacotados |
| `PackedStringArray`, `PackedVector2Array`, `PackedVector3Array` | Arrays empacotados |
| `PackedColorArray`, `PackedVector4Array` | Arrays empacotados |

#### Array e Dictionary

Ambos são implementados usando Variant internamente:

```gdscript
# Array — qualquer tipo de Variant
var arr: Array = [1, "dois", Vector2(3, 4)]

# Dictionary — chave e valor podem ser qualquer Variant
var d: Dictionary = {"nome": "Alice", 42: true}

# Modificações afetam todas as referências (semântica de referência compartilhada)
var a = arr
a.append("extra")   # arr também é modificado
```

**Regra:** Em ambiente multithread, crie um `Mutex` antes de modificar Arrays ou Dictionaries compartilhados.

> ⚠ Evite: Armazenar `Array` ou `Dictionary` sem considerar que são tipos de referência — cópias superficiais (`arr2 = arr`) não duplicam o conteúdo.

---

### 41.5 Object class

#### Definição e macro GDCLASS

`Object` é a classe base de quase tudo no Godot. Herdar dela requer a macro `GDCLASS`:

```cpp
class CustomObject : public Object {
    GDCLASS(CustomObject, Object);
    // ...
};

// Instanciar e inspecionar
CustomObject *obj = memnew(CustomObject);
print_line("Classe: ", obj->get_class());

// Cast dinâmico (não usa RTTI do C++)
OtherClass *obj2 = Object::cast_to<OtherClass>(obj); // nullptr se falhar
```

#### Registrando classes

```cpp
// Registro público e instanciável via ClassDB (scripts, serialização)
GDREGISTER_CLASS(MinhaClasse);

// Público mas sem instanciação automática
GDREGISTER_VIRTUAL_CLASS(MinhaClasse);

// Público mas sem nenhuma instanciação via ClassDB
GDREGISTER_ABSTRACT_CLASS(MinhaClasse);

// Privado — não visível a scripts/extensões
GDREGISTER_INTERNAL_CLASS(MinhaClasse);

// Só disponível em runtime (não no editor)
GDREGISTER_RUNTIME_CLASS(MinhaClasse);
```

#### Registrando bindings (_bind_methods)

```cpp
static void _bind_methods() {
    // Método com argumentos nomeados
    ClassDB::bind_method(
        D_METHOD("meu_metodo", "arg1", "arg2"),
        &MinhaClasse::meu_metodo,
        DEFVAL(-1)  // default para arg2
    );

    // Constante de enum
    VARIANT_ENUM_CAST(MinhaClasse::MeuEnum);
    BIND_CONSTANT(MODO_A);
    BIND_CONSTANT(MODO_B);

    // Propriedade com getter/setter
    ADD_PROPERTY(
        PropertyInfo(Variant::INT, "quantidade",
                     PROPERTY_HINT_RANGE, "0,100,1"),
        "set_quantidade", "get_quantidade"
    );

    // Sinal
    ADD_SIGNAL(MethodInfo("foi_destruido"));
}
```

**Regra:** `D_METHOD()` é removido em builds de release — use-o sempre para nomear argumentos em Debug.

#### Ownership e casting

```cpp
// Objetos não-RefCounted: gerenciamento manual
Node *node = memnew(Node);
memdelete(node);   // liberar explicitamente

// Armazenar por ObjectID quando não é dono exclusivo
ObjectID id = node->get_instance_id();
Object *talvez = ObjectDB::get_instance(id);
ERR_FAIL_NULL(talvez);  // pode ter sido liberado

// Objetos RefCounted: gerenciamento por contagem de referência
Ref<MinhaRefCounted> ref = memnew(MinhaRefCounted);
// liberado automaticamente quando o último Ref sai de escopo

// Cast seguro via Variant (deferred callbacks)
void callback(Variant p_var) {
    Object *obj = p_var.get_validated_object();
    ERR_FAIL_NULL(obj);
}
```

> ⚠ Evite: Armazenar `RefCounted*` como ponteiro bruto — use sempre `Ref<T>`. Evite chamar `memdelete` em `RefCounted`.

#### Notificações

Todos os Objects respondem a `_notification(int what)`. As notificações são propagadas pela hierarquia:

```gdscript
# GDScript
func _notification(what: int) -> void:
    match what:
        NOTIFICATION_READY:
            pass
        NOTIFICATION_PROCESS:
            pass
        NOTIFICATION_EXIT_TREE:
            pass
```

#### Resources

`Resource` herda de `RefCounted` — todas as resources são reference-counted. Uma Resource pode referenciar um arquivo em disco (`res://`).

```cpp
// Carregar resource (retorna referência em cache se já carregada)
Ref<Resource> res = ResourceLoader::load("res://minha.res");

// Salvar resource
ResourceSaver::save("res://minha.res", instancia);
```

**Regra:** Dois Resources diferentes não podem ter o mesmo path de arquivo. Sub-resources sem path são salvas junto com a Resource principal (recebem IDs como `res://arquivo.res::1`).

---

### 41.6 Inheritance Class Tree

Hierarquia das principais raízes da árvore de classes do Godot:

```
Object
├── RefCounted
│   ├── Resource           (arquivos em disco, reference-counted)
│   │   ├── Script
│   │   ├── Texture2D
│   │   ├── Mesh
│   │   └── ...
│   └── ...
└── Node                   (árvore de cena, gerenciamento manual)
    ├── Control            (UI — âncoras, temas, foco)
    │   ├── Button
    │   ├── Label
    │   ├── Container
    │   └── ...
    ├── Node2D             (espaço 2D — Transform2D herdado)
    │   ├── Sprite2D
    │   ├── CollisionShape2D
    │   └── ...
    └── Node3D             (espaço 3D — Transform3D herdado)
        ├── MeshInstance3D
        ├── Camera3D
        ├── Light3D
        └── ...
```

| Classe raiz | Herda de | Característica principal |
|-------------|----------|------------------------|
| `Object` | — | Base de tudo; reflection, ClassDB, signals, properties |
| `RefCounted` | Object | Gerenciamento automático por contagem de referência |
| `Resource` | RefCounted | Persistência em disco, cache por path, sub-resources |
| `Node` | Object | Árvore de cena, ciclo de vida (_ready, _process, _input), groups |
| `Control` | CanvasItem → Node | Interface do usuário, âncoras, temas, foco de input |
| `Node2D` | CanvasItem → Node | Transformações 2D (posição, rotação, escala em espaço 2D) |
| `Node3D` | Node | Transformações 3D (Transform3D, Basis), hierarquia espacial |

**Regra:** Em GDScript, herde da classe mais específica para o seu propósito — `Node2D` para lógica 2D, `Control` para UI, `Node3D` para objetos 3D, `RefCounted` para dados puros sem necessidade de estar na cena.

> ⚠ Evite: Herdar de `Object` diretamente em GDScript quando `RefCounted` seria suficiente — objetos `Object` não têm gerenciamento automático de memória.

---

## 42 Unit Testing C++

Godot integra o framework **doctest** para testes unitários em C++. Os testes vivem em `tests/` na raiz do repositório e só compilam com `tests=yes`.

### 42.1 Plataformas, Build e Execução

```bash
# Compilar com testes habilitados
scons tests=yes

# Rodar todos os testes
./bin/<godot_binary> --test

# Listar opções disponíveis
./bin/<godot_binary> --test --help
```

**Filtragem:**

| Opção | Atalho | Exemplo |
|-------|--------|---------|
| `--test-suite` | `-ts` | `-ts="*[GDScript]*"` |
| `--test-case` | `-tc` | `-tc="*[String]*"` |
| `--source-file` | `-sf` | `-sf="*test_color*"` |

```bash
# Rodar apenas os testes de String com output de sucesso
./bin/<godot_binary> --test --test-case="*[String]*" --success

# Pular testes de stress
./bin/<godot_binary> --test --test-case-exclude="*[Stress]*"

# Redirecionar output para XML
./bin/<godot_binary> --test --source-file="*test_validate*" --reporters=xml --out=doctest.txt
```

> ⚠ Com `dev_mode=yes`, testes são compilados automaticamente e warnings viram erros.

### 42.2 Escrevendo Testes (TEST_CASE / SUBCASE)

Arquivos de teste ficam em `tests/`, prefixados com `test_`, e devem ser incluídos em `tests/test_main.cpp`.

```cpp
#pragma once
#include "tests/test_macros.h"

namespace TestString {

TEST_CASE("[String] Hello World!") {
    String hello = "Hello World!";
    CHECK(hello == "Hello World!");
}

} // namespace TestString
```

**SUBCASE** — setup comum com variações:

```cpp
TEST_CASE("[SceneTree][Node] Operações com scene tree simples") {
    // setup comum aqui
    SUBCASE("Mover node para índice específico") {
        // setup + checks para move
    }
    SUBCASE("Remover node em índice específico") {
        // setup + checks para remove
    }
}
```

Cada `SUBCASE` faz o `TEST_CASE` recomeçar do início. Subcases podem ser aninhados (limite recomendado: 1 nível).

> Use `tests/create_test.py -i` para gerar boilerplate automaticamente.

### 42.3 Assertions e Logging

**Assertions (por severidade):**

| Macro | Comportamento |
|-------|--------------|
| `REQUIRE` / `REQUIRE_FALSE` | Falha imediatamente se condição não passa |
| `CHECK` / `CHECK_FALSE` | Marca como falha mas continua |
| `WARN` / `WARN_FALSE` | Apenas loga aviso, nunca falha |

Todas têm variantes `*_MESSAGE(cond, "mensagem")` para explicações adicionais.

**Logging:**

| Macro | Descrição |
|-------|-----------|
| `MESSAGE` | Imprime mensagem |
| `FAIL_CHECK` | Marca como falha, continua |
| `FAIL` | Falha imediatamente |

**Testando caminhos de falha (ERR_PRINT_OFF/ON):**

```cpp
TEST_CASE("[Color] Construtor com HTML inválido") {
    ERR_PRINT_OFF;
    Color html_invalid = Color::html("invalid");
    ERR_PRINT_ON; // Sempre reabilitar!

    CHECK_MESSAGE(html_invalid.is_equal_approx(Color()),
        "HTML inválido deve resultar em Color padrão.");
}
```

### 42.4 Tags Especiais e Testing de Signals

**Tags no nome do test case:**

| Tag | Ambiente adicionado |
|-----|-------------------|
| `[SceneTree]` | Scene tree com MessageQueue, mock rendering server, ThemeDB |
| `[Editor]` | Como `[SceneTree]` + EditorSettings e infraestrutura do editor |
| `[Audio]` | AudioServer com driver mock |
| `[Navigation2D]` | Servidor de navegação 2D padrão |
| `[Navigation3D]` | Servidor de navegação 3D padrão |

**Macros para signals:**

```cpp
SIGNAL_WATCH(objeto, "nome_do_signal");
SIGNAL_CHECK("nome_do_signal", Vector<Vector<Variant>>{{}}); // outer = emissões, inner = args
SIGNAL_CHECK_FALSE("nome_do_signal");
SIGNAL_DISCARD("nome_do_signal");
SIGNAL_UNWATCH(objeto, "nome_do_signal");
```

Exemplo:

```cpp
SIGNAL_WATCH(test_timer, SNAME("timeout"));
test_timer->start(0.1);
SceneTree::get_singleton()->process(0.2);
Array signal_args;
signal_args.push_back(Array());
SIGNAL_CHECK(SNAME("timeout"), signal_args);
SIGNAL_UNWATCH(test_timer, SNAME("timeout"));
```

### 42.5 Test Tools (REGISTER_TEST_COMMAND)

Test tools são procedimentos manuais de debug registráveis como comandos `--test`:

```cpp
// Em register_types.cpp do módulo
#ifdef TESTS_ENABLED
void test_tokenizer() {
    TestGDScript::test(TestGDScript::TestType::TEST_TOKENIZER);
}
REGISTER_TEST_COMMAND("gdscript-tokenizer", &test_tokenizer);
#endif
```

```bash
./bin/<godot_binary> --test gdscript-tokenizer test.gd
```

Se uma tool for detectada, os testes unitários são pulados.

### 42.6 Integration Tests para GDScript

Para testar o próprio compilador/parser do GDScript:

1. Criar script em `modules/gdscript/tests/scripts/` com função `test()` sem argumentos.
2. Gerar arquivos `.out` esperados:
   ```bash
   bin/<godot_binary> --gdscript-generate-tests modules/gdscript/tests/scripts
   ```
3. Rodar os testes:
   ```bash
   ./bin/<godot_binary> --test --test-suite="*GDScript*"
   ```

> Scripts sem `test()` devem ter nome `*.notest.gd` para desabilitar a execução em runtime.

---

## 43 Custom Modules C++

### 43.1 Quando usar Módulos vs GDExtension

| Situação | Recomendação |
|----------|-------------|
| Lógica de jogo customizada | GDExtension (não requer recompilação) |
| Binding de biblioteca externa (PhysX, FMOD) | Módulo C++ |
| Otimizar partes críticas | Módulo C++ |
| Adicionar funcionalidade ao editor/engine | Módulo C++ |
| Integração profunda com o core | Módulo C++ |

### 43.2 Estrutura de um Módulo (Arquivos Obrigatórios)

```
modules/summator/
├── config.py          # can_build / configure
├── summator.h         # declaração da classe com GDCLASS
├── summator.cpp       # implementação + _bind_methods
├── register_types.h   # initialize_*/uninitialize_* declarations
├── register_types.cpp # ClassDB::register_class<>()
└── SCsub              # instrui SCons a compilar os .cpp
```

**summator.h:**
```cpp
#pragma once
#include "core/object/ref_counted.h"

class Summator : public RefCounted {
    GDCLASS(Summator, RefCounted);
    int count;
protected:
    static void _bind_methods();
public:
    void add(int p_value);
    void reset();
    int get_total() const;
    Summator();
};
```

**summator.cpp:**
```cpp
#include "summator.h"

void Summator::add(int p_value) { count += p_value; }
void Summator::reset() { count = 0; }
int Summator::get_total() const { return count; }

void Summator::_bind_methods() {
    ClassDB::bind_method(D_METHOD("add", "value"), &Summator::add);
    ClassDB::bind_method(D_METHOD("reset"), &Summator::reset);
    ClassDB::bind_method(D_METHOD("get_total"), &Summator::get_total);
}

Summator::Summator() { count = 0; }
```

**register_types.cpp:**
```cpp
#include "register_types.h"
#include "core/object/class_db.h"
#include "summator.h"

void initialize_summator_module(ModuleInitializationLevel p_level) {
    if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) return;
    ClassDB::register_class<Summator>();
}
void uninitialize_summator_module(ModuleInitializationLevel p_level) {}
```

**SCsub:**
```python
Import('env')
env.add_source_files(env.modules_sources, "*.cpp")
```

**config.py:**
```python
def can_build(env, platform): return True
def configure(env): pass
```

### 43.3 Compilando e Usando o Módulo

```bash
scons  # módulo em modules/ é detectado automaticamente
```

No GDScript:
```gdscript
var s = Summator.new()
s.add(10)
s.add(20)
print(s.get_total())  # 30
```

> ⚠ Para exportar projetos com módulo customizado, recompile também os export templates e aponte o caminho no export preset.

**Flags de compilação por módulo (sem poluir o build todo):**
```python
# SCsub
Import('env')
module_env = env.Clone()
module_env.add_source_files(env.modules_sources, "*.cpp")
module_env.Append(CCFLAGS=['-O2'])
```

**Paths de include:**
```python
env.Append(CPPPATH=["mylib/include"])      # relativo
env.Append(CPPPATH=["#myotherlib/include"]) # absoluto
```

**Linkando bibliotecas externas pré-compiladas (.a/.lib):**
```python
# SCsub — use env.Clone() para não poluir o build global
Import('env')
env_tts = env.Clone()
env_tts.add_source_files(env.modules_sources, '*.cpp')
env_tts.Append(CPPPATH=['mylib/include', 'speech_tools/include'])

# LIBPATH e LIBS devem ir em env (não no clone) para linkar ao binário final
env.Append(LIBPATH=[Dir('libpath').abspath])  # diretório com .a/.lib
env.Append(LIBS=['Festival', 'estools', 'estbase', 'eststring'])
```

> 💡 Para incluir uma biblioteca externa como código-fonte no repositório do módulo, use `git submodule` dentro do diretório do módulo. Não use submodules para módulos destinados ao repositório principal do Godot — prefira GDExtension nesses casos.

### 43.4 Compilação Externa (custom_modules)

Para manter o módulo fora do repositório do Godot:

```bash
# Mover módulo para diretório externo
mv modules/summator ../my_modules/

# Compilar apontando o diretório
scons custom_modules=../my_modules
```

O build system detecta todos os módulos sob `../my_modules/` automaticamente. Aceita lista separada por vírgula para múltiplos diretórios.

Para desabilitar um módulo durante build: `module_summator_enabled=no`.

### 43.5 Ordem de Inicialização (preregister)

Ordem padrão de registro durante startup:

```
preregister_module_types()
preregister_server_types()
register_core_singletons()
register_server_types()
register_scene_types()
EditorNode::register_editor_types()
register_module_types()      ← Summator é registrado aqui por padrão
...
```

Para registrar **antes** de qualquer outro tipo (ex.: singletons de dependência):

**register_types.h:**
```cpp
#define MODULE_SUMMATOR_HAS_PREREGISTER  // define explícito obrigatório
void preregister_summator_module(ModuleInitializationLevel p_level);
void initialize_summator_module(ModuleInitializationLevel p_level);
void uninitialize_summator_module(ModuleInitializationLevel p_level);
```

```cpp
void preregister_summator_module(ModuleInitializationLevel p_level) {
    // Executado antes de qualquer tipo core ser registrado
}
```

### 43.6 Documentação e Ícones Customizados

**Documentação:**
1. Criar `modules/summator/doc_classes/`.
2. Em `config.py`:
   ```python
   def get_doc_path(): return "doc_classes"
   def get_doc_classes(): return ["Summator"]
   ```
3. Gerar XML base: `bin/<godot_binary> --doctool .`
4. Editar `doc_classes/Summator.xml` conforme o class reference primer.
5. Recompilar — docs ficam acessíveis no sistema de documentação interno.

**Ícones customizados:**
1. Criar `modules/summator/icons/` com SVGs otimizados.
2. Recompilar e rodar o editor — ícones aparecem automaticamente.
3. Path alternativo: `config.py` → `def get_icons_path(): return "path/to/icons"`.

### 43.7 Unit Tests em Módulos

```bash
mkdir modules/summator/tests
```

Criar `test_summator.h` (prefixo `test_` obrigatório):

```cpp
#pragma once
#include "tests/test_macros.h"
#include "modules/summator/summator.h"

namespace TestSummator {

TEST_CASE("[Modules][Summator] Somando números") {
    Ref<Summator> s = memnew(Summator);
    CHECK(s->get_total() == 0);
    s->add(10); CHECK(s->get_total() == 10);
    s->add(20); CHECK(s->get_total() == 30);
    s->reset(); CHECK(s->get_total() == 0);
}

} // namespace TestSummator
```

```bash
scons tests=yes
./bin/<godot_binary> --test --source-file="*test_summator*" --success
```

### 43.8 Regras e Sumário

- Use `GDCLASS(MinhaClasse, ClassePai)` para herança — obrigatório para registro no ClassDB.
- Implemente `static void _bind_methods()` para expor métodos ao scripting e como callbacks de signals.
- **Não use multiple inheritance** em classes expostas ao Godot — `GDCLASS` não suporta. Multiple inheritance é OK em classes internas não expostas.
- Herdando de `Node`: a classe aparece no editor em "Add Node".
- Herdando de `Resource`: aparece na lista de resources, propriedades expostas são serializadas.
- Módulos permitem estender o editor e qualquer área do engine.

---

## 44. Custom Godot Servers (C++)

Servidores Godot são singletons de thread separada que implementam o padrão mediator — gerenciam dados via RIDs, processam em background e expõem API ao scripting. Use para: AI, protocolos de rede, dispositivos de input, VoIP, threads assíncronas customizadas.

### 44.1 Estrutura de um Server

Componentes mínimos: instância estática, Thread, Mutex, flag `exit_thread`, `init()` e `finish()`.

```cpp
// hilbert_hotel.h
#include "core/object/object.h"
#include "core/os/thread.h"
#include "core/os/mutex.h"
#include "core/templates/rid.h"

class HilbertHotel : public Object {
    GDCLASS(HilbertHotel, Object);
    static HilbertHotel *singleton;
    static void thread_func(void *p_udata);

    bool exit_thread = false;
    Thread *thread   = nullptr;
    Mutex  *mutex    = nullptr;
    RID_Owner<InfiniteBus> bus_owner;
public:
    static HilbertHotel *get_singleton();
    Error init();
    void lock();
    void unlock();
    void finish();
protected:
    static void _bind_methods();
};
```

```cpp
// loop da thread
void HilbertHotel::thread_func(void *p_udata) {
    HilbertHotel *ac = (HilbertHotel *)p_udata;
    while (!ac->exit_thread) {
        if (!ac->empty()) {
            ac->lock();
            ac->register_rooms();
            ac->unlock();
        }
        OS::get_singleton()->delay_usec(1000 * 1000); // 1s
    }
}

Error HilbertHotel::init() {
    mutex = Mutex::create();
    thread = Thread::create(HilbertHotel::thread_func, this);
    return OK;
}
void HilbertHotel::finish() {
    if (!thread) return;
    exit_thread = true;
    Thread::wait_to_finish(thread);
    memdelete(thread);
    if (mutex) memdelete(mutex);
    thread = nullptr;
}
```

**Regra**: sempre chame `lock()`/`unlock()` ao redor de toda leitura/escrita em dados compartilhados entre a thread do server e a SceneTree.

### 44.2 RID-Based Resource Data

Recursos gerenciados pelo server herdam `RID_Data`; o server usa `RID_Owner<T>` para criar, acessar e liberar RIDs.

```cpp
class InfiniteBus : public RID_Data {
    RID self;
    uint64_t prime_num, num;
public:
    uint64_t next_room() { return prime_num * num++; }
    void set_self(const RID &p_self) { self = p_self; }
    RID  get_self() const { return self; }
    InfiniteBus(uint64_t prime) : prime_num(prime), num(1) {}
};
```

```cpp
RID HilbertHotel::create_bus() {
    lock();
    InfiniteBus *ptr = memnew(InfiniteBus(PRIME[counter++]));
    RID ret = bus_owner.make_rid(ptr);  // server assume ownership
    ptr->set_self(ret);
    buses.insert(ret);
    unlock();
    return ret;
}
bool HilbertHotel::delete_bus(RID id) {
    if (bus_owner.owns(id)) {
        lock();
        InfiniteBus *b = bus_owner.get(id);
        bus_owner.free(id);
        buses.erase(id);
        memdelete(b);
        unlock();
        return true;
    }
    return false;
}
```

### 44.3 Dummy Class e GDScript Binding

O construtor do server define o singleton estático antes do GDScript existir; expor a classe diretamente causaria binding incorreto. Crie uma **classe dummy** (`_HilbertHotel`) que delega ao singleton real e é registrada via `Engine::add_singleton`.

```cpp
// register_types.cpp
static HilbertHotel  *hilbert_hotel  = nullptr;
static _HilbertHotel *_hilbert_hotel = nullptr;

void register_hilbert_hotel_types() {
    hilbert_hotel = memnew(HilbertHotel);
    hilbert_hotel->init();
    _hilbert_hotel = memnew(_HilbertHotel);
    ClassDB::register_class<_HilbertHotel>();
    Engine::get_singleton()->add_singleton(
        Engine::Singleton("HilbertHotel", _HilbertHotel::get_singleton()));
}
void unregister_hilbert_hotel_types() {
    if (hilbert_hotel) { hilbert_hotel->finish(); memdelete(hilbert_hotel); }
    if (_hilbert_hotel) memdelete(_hilbert_hotel);
}
```

Métodos da dummy delegam ao singleton; signals são emitidos via dummy:

```cpp
Variant _HilbertHotel::get_bus_info(RID id) {
    return HilbertHotel::get_singleton()->get_bus_info(id);
}
// server chama isso na sua thread para emitir signal no GDScript
void HilbertHotel::_emit_occupy_room(uint64_t room, RID rid) {
    _HilbertHotel::get_singleton()->_occupy_room(room, rid);
}
void _HilbertHotel::_occupy_room(int room, RID bus) {
    emit_signal("occupy_room", room, bus);
}
```

```gdscript
func _ready():
    HilbertHotel.occupy_room.connect(_on_room)
    var rid = HilbertHotel.create_bus()
    await get_tree().create_timer(2.0).timeout
    print(HilbertHotel.get_bus_info(rid))
    HilbertHotel.delete_bus(rid)
```

### 44.4 MessageQueue

Para enviar comandos da thread do server à SceneTree sem locks manuais, use `MessageQueue`:

```cpp
MessageQueue::get_singleton()->push_call(obj, "method_name", arg1, arg2);
MessageQueue::get_singleton()->push_set(obj, "property", value);
MessageQueue::get_singleton()->push_notification(obj, NOTIFICATION_READY);
```

A fila é esvaziada automaticamente em `SceneTree::idle` e `SceneTree::iteration` — os comandos são executados na main thread no próximo frame.

---

## 45. Custom Resource Format Loaders

`ResourceFormatLoader` é a interface de fábrica para suportar novos formatos de arquivo. Recursos carregados são cacheados — múltiplas chamadas `load()` para o mesmo path retornam o mesmo objeto, logo **recursos devem ser stateless**.

> ⚠ Evite: usar `ResourceFormatLoader` para imagens raster — use `ImageFormatLoader` (core/io/image_loader.h).

Usos típicos: formatos de áudio, vídeo, modelos de machine learning, arquivos de dados customizados.

### 45.1 ResourceFormatLoader

```cpp
// resource_loader_json.h
#include "core/io/resource_loader.h"

class ResourceFormatLoaderJson : public ResourceFormatLoader {
    GDCLASS(ResourceFormatLoaderJson, ResourceFormatLoader);
public:
    virtual RES  load(const String &p_path, const String &p_original_path, Error *r_error = nullptr);
    virtual void get_recognized_extensions(List<String> *r_extensions) const;
    virtual bool handles_type(const String &p_type) const;
    virtual String get_resource_type(const String &p_path) const;
};
```

```cpp
RES ResourceFormatLoaderJson::load(const String &p_path, const String &, Error *r_error) {
    Ref<JsonResource> json = memnew(JsonResource);
    if (r_error) *r_error = OK;
    json->load_file(p_path);
    return json;
}
void ResourceFormatLoaderJson::get_recognized_extensions(List<String> *r) const {
    if (!r->find("json")) r->push_back("json");
}
String ResourceFormatLoaderJson::get_resource_type(const String &) const { return "Resource"; }
bool   ResourceFormatLoaderJson::handles_type(const String &p_type) const {
    return ClassDB::is_parent_class(p_type, "Resource");
}
```

### 45.2 ResourceFormatSaver

```cpp
class ResourceFormatSaverJson : public ResourceFormatSaver {
    GDCLASS(ResourceFormatSaverJson, ResourceFormatSaver);
public:
    virtual Error save(const String &p_path, const RES &p_resource, uint32_t p_flags = 0);
    virtual bool  recognize(const RES &p_resource) const;
    virtual void  get_recognized_extensions(const RES &p_resource, List<String> *r_extensions) const;
};
```

```cpp
Error ResourceFormatSaverJson::save(const String &p_path, const RES &p_resource, uint32_t) {
    Ref<JsonResource> json = memnew(JsonResource);
    return json->save_file(p_path, p_resource);
}
bool ResourceFormatSaverJson::recognize(const RES &p_resource) const {
    return Object::cast_to<JsonResource>(*p_resource) != nullptr;
}
```

### 45.3 Custom Data Type e Registro

```cpp
class JsonResource : public Resource {
    GDCLASS(JsonResource, Resource);
    Dictionary content;
protected:
    static void _bind_methods() {
        ClassDB::bind_method(D_METHOD("set_dict", "dict"), &JsonResource::set_dict);
        ClassDB::bind_method(D_METHOD("get_dict"), &JsonResource::get_dict);
        ADD_PROPERTY(PropertyInfo(Variant::DICTIONARY, "content"), "set_dict", "get_dict");
    }
public:
    Error      load_file(const String &p_path);
    Error      save_file(const String &p_path, const RES &p_resource);
    void       set_dict(const Dictionary &d) { content = d; }
    Dictionary get_dict() { return content; }
};
```

Registro no módulo:

```cpp
static Ref<ResourceFormatLoaderJson> json_loader;
static Ref<ResourceFormatSaverJson>  json_saver;

void register_json_types() {
    ClassDB::register_class<JsonResource>();
    json_loader.instantiate();
    ResourceLoader::add_resource_format_loader(json_loader);
    json_saver.instantiate();
    ResourceSaver::add_resource_format_saver(json_saver);
}
void unregister_json_types() {
    ResourceLoader::remove_resource_format_loader(json_loader);
    json_loader.unref();
    ResourceSaver::remove_resource_format_saver(json_saver);
    json_saver.unref();
}
```

```gdscript
@onready var data = load("res://demo.json")
func _ready():
    print(data.get_dict())
```

> 💡 Para bibliotecas externas que usam `std::istream`, crie um adaptador `GodotFileInStreamBuf : public std::streambuf` que traduz `FileAccess::get_8()` para a interface de stream C++.

---

## 46. Custom AudioStreams (C++)

Para integrar engines de áudio externos (FMOD, Wwise), formatos customizados ou geradores procedurais de PCM, crie um par `AudioStream` + `AudioStreamPlayback`.

- **`AudioStream`**: data container, exposto ao GDScript. Se carregado via ResourceLoader, **deve ser stateless** — estado de reprodução vai em `AudioStreamPlayback`.
- **`AudioStreamPlayback`**: criado por `instance_playback()`; contém buffer PCM, posição e flag `active`.

### 46.1 AudioStream + AudioStreamPlayback

```cpp
class AudioStreamMyTone : public AudioStream {
    GDCLASS(AudioStreamMyTone, AudioStream)
    friend class AudioStreamPlaybackMyTone;
    int mix_rate = 44100, hz = 639;
    uint64_t pos = 0;
public:
    virtual Ref<AudioStreamPlayback> instance_playback();
    virtual String get_stream_name() const { return "MyTone"; }
    virtual float  get_length() const { return 0; }
    void gen_tone(int16_t *pcm_buf, int size);
    void reset() { pos = 0; }
    void set_position(uint64_t p) { pos = p; }
protected:
    static void _bind_methods();
};

Ref<AudioStreamPlayback> AudioStreamMyTone::instance_playback() {
    Ref<AudioStreamPlaybackMyTone> pb;
    pb.instantiate();
    pb->base = Ref<AudioStreamMyTone>(this);
    return pb;
}
void AudioStreamMyTone::gen_tone(int16_t *buf, int size) {
    for (int i = 0; i < size; i++)
        buf[i] = (int16_t)(32767.0 * Math::sin(Math_TAU * double(pos + i) / (double(mix_rate) / hz)));
    pos += size;
}
```

```cpp
class AudioStreamPlaybackMyTone : public AudioStreamPlayback {
    GDCLASS(AudioStreamPlaybackMyTone, AudioStreamPlayback)
    enum { PCM_BUFFER_SIZE = 4096 };
    void *pcm_buffer = nullptr;
    Ref<AudioStreamMyTone> base;
    bool active = false;
public:
    AudioStreamPlaybackMyTone() {
        AudioServer::get_singleton()->lock();
        pcm_buffer = AudioServer::get_singleton()->audio_data_alloc(PCM_BUFFER_SIZE);
        zeromem(pcm_buffer, PCM_BUFFER_SIZE);
        AudioServer::get_singleton()->unlock();
    }
    ~AudioStreamPlaybackMyTone() {
        if (pcm_buffer) AudioServer::get_singleton()->audio_data_free(pcm_buffer);
    }
    virtual void mix(AudioFrame *p_buffer, float, int p_frames) override {
        ERR_FAIL_COND(!active);
        zeromem(pcm_buffer, PCM_BUFFER_SIZE);
        int16_t *buf = (int16_t *)pcm_buffer;
        base->gen_tone(buf, p_frames);
        for (int i = 0; i < p_frames; i++) {
            float s = float(buf[i]) / 32767.0f;
            p_buffer[i] = AudioFrame(s, s);
        }
    }
    virtual void  start(float p = 0.0) { seek(p); active = true; }
    virtual void  stop()  { active = false; base->reset(); }
    virtual bool  is_playing() const { return active; }
    virtual int   get_loop_count() const { return 0; }
    virtual float get_playback_position() const { return 0.0f; }
    virtual float get_length() const { return 0.0f; }
    virtual void  seek(float t) { base->set_position(uint64_t(t * base->mix_rate) << 13); }
};
```

> ⚠ `mix()` roda na **audio thread** — proibido I/O, alocação dinâmica ou locks de SceneTree. Aloque o PCM buffer no construtor via `audio_data_alloc`/`audio_data_free`.

### 46.2 Resampling (AudioStreamPlaybackResampled)

Quando o sample rate difere de 44100 Hz, use `AudioStreamPlaybackResampled` (Godot aplica interpolação cúbica automaticamente):

```cpp
class AudioStreamPlaybackResampledMyTone : public AudioStreamPlaybackResampled {
    GDCLASS(AudioStreamPlaybackResampledMyTone, AudioStreamPlaybackResampled)
protected:
    virtual void _mix_internal(AudioFrame *p_buffer, int p_frames) override;
public:
    virtual float get_stream_sampling_rate() override { return float(base->mix_rate); }
    // implementar: start/stop/is_playing/get_loop_count/get_playback_position/seek/get_length
};
```

`_mix_internal` substitui `mix` — o Godot chama `_mix_internal` e aplica o resampling antes de entregar ao AudioServer. `get_stream_sampling_rate()` informa a taxa real do stream para o resampler.

---

## 47. Custom Platform Ports (C++)

Platform ports permitem adicionar suporte a uma nova plataforma sem modificar o código-fonte existente do Godot — o mesmo princípio dos módulos C++. Todo o código fica em `platform/<nome>/`.

### 47.1 Visão Geral e Requisitos de RAM

- Um port customizado é necessário quando: (a) você quer portar para consoles escrevendo a camada de plataforma você mesmo (requer NDA com o fabricante) ou (b) a plataforma-alvo não é suportada oficialmente.
- **Requisito mínimo de RAM**: ~100 MB em projeto vazio no Linux (50 MB no modo headless). Plataformas com severa limitação de memória precisarão de versões mais antigas do Godot.

> ⚠ Evite: tentar rodar Godot 4 em retro-consoles ou plataformas embedded com < 64 MB de RAM — o overhead do engine o torna inviável.

### 47.2 Arquivos Obrigatórios (OS singleton + detect.py + logo.svg)

**OS singleton**: herde de `OS` (ou `OS_Unix` se UNIX-like) e implemente os métodos requeridos. Ver `platform/linuxbsd/os_linuxbsd.cpp` como referência.

**detect.py** — obrigatório para o SCons reconhecer a plataforma. Deve implementar:

```python
def is_active():    return True           # False desativa temporariamente o build
def get_name():     return "myplatform"   # nome exibido ao usuário
def can_build():    return True/False     # não fazer checagens lentas aqui
def get_opts():     return [...]          # opções SCons da plataforma
def get_flags():    return [...]          # flags SCons sobrescritas
def configure(env): ...                   # configuração de compilador, dependências
```

**logo.svg**: imagem vetorial 32×32 exibida no diálogo de Export.

**Regra**: implemente pelo menos OS singleton + `detect.py` + `logo.svg` para a plataforma ser compilável em modo headless.

### 47.3 Features Opcionais

| Feature | Classe/Arquivo de referência |
|---|---|
| Janelas e mouse/touch | `DisplayServer` (subclasse) |
| Renderização Vulkan | `RenderingContextDriverVulkan` |
| Renderização D3D12 | `RenderingContextDriverD3D12` |
| Renderização OpenGL/ES | `GLManager` |
| Teclado e controle | `KeyMappingX11`, `JoypadLinux` (refs Linux) |
| Áudio | Subclasse de `AudioDriver` (em `platform/` ou `drivers/`) |
| Crash handler | Imprimir backtrace na crash |
| TTS | Text-to-speech (acessibilidade) |
| Export handler | `EditorExportPlatform` + `run_icon.svg` (16×16) |

Se a plataforma não suporta Vulkan/D3D12/OpenGL, as opções são:
- Usar biblioteca de tradução em runtime (ex.: MoltenVK no macOS → Metal).
- Criar um renderer do zero (custo muito alto).

### 47.4 Distribuição

**Regra**: distribua o port como uma pasta `platform/<nome>/` que pode ser clonada diretamente dentro do repositório Godot. Build:

```sh
scons platform=<nome>
```

Se um driver de renderização customizado for necessário, adicione também uma pasta em `drivers/`. Nesse caso, distribua como fork do repositório Godot ou como coleção de pastas aplicadas sobre um clone.

> ⚠ Evite: distribuir código de SDK de console publicamente — SDKs de console geralmente estão sob NDA que proíbe redistribuição.

---

## 48. Build do Engine (Compilação a partir do Código-Fonte)

### 48.1 Sistema de Build (SCons)

Godot usa **SCons** como sistema de build. Um build padrão para a plataforma atual é:

```sh
scons
```

Isso produz um binário editor para a plataforma/OS/arch atual. Nome do binário resultante (em `bin/`):

```
godot.<platform>.<target>[.dev][.double].<arch>[.<ext>]
# Ex: godot.linuxbsd.editor.x86_64
```

**Opções universais fundamentais:**

| Opção | Valores | Descrição |
|---|---|---|
| `target` | `editor`, `template_debug`, `template_release` | Tipo de binário |
| `platform` | `windows`, `linuxbsd`, `macos`, `android`, `ios`, `web` | Plataforma alvo |
| `arch` | `auto`, `x86_32`, `x86_64`, `arm32`, `arm64`, `rv64`, ... | Arquitetura |
| `dev_build=yes` | — | Desativa otimizações, habilita DEV_ENABLED, gera símbolos de debug |
| `debug_symbols=yes` | — | Inclui símbolos de debug no binário (necessário para profilers/crash traces) |
| `optimize` | `speed_trace`(padrão), `speed`, `size`, `size_extra`, `debug`, `none` | Nível de otimização |
| `-j<N>` | número | Threads de compilação (padrão: todos exceto um) |

**Aliases de conveniência:**
- `dev_mode=yes` → `verbose=yes warnings=extra werror=yes tests=yes`
- `production=yes` → `use_static_cpp=yes debug_symbols=no lto=auto`

**Customização via arquivo `custom.py`** (na raiz do repositório):

```python
optimize = "size"
module_mono_enabled = "yes"
use_llvm = "yes"
extra_suffix = "my_game"
```

Também se usa `SCONSFLAGS` para definir opções globais no ambiente (ex.: `export SCONSFLAGS="-j4"`).

**SCU (Single Compilation Unit) build** — acelera desenvolvimento agrupando múltiplos `.cpp` em uma única translation unit:

```sh
scons scu_build=yes
```

> ⚠ Antes de submeter um PR, fazer um build regular (sem SCU) pois SCU pode mascarar includes faltando.

**Limpeza de arquivos gerados:**

```sh
scons --clean <options>
# ou
git clean -fixd   # remove TODOS os arquivos não rastreados e ignorados
```

### 48.2 Targets e Plataformas

```sh
scons platform=<platform> target=editor|template_debug|template_release
```

Listar plataformas disponíveis: `scons platform=list`

**Export templates**: para distribuir, é preciso compilar templates para cada plataforma. O arquivo `version.txt` dentro do pacote de templates deve conter o identificador de versão (ex.: `4.4.1.stable`).

### 48.3 Opções de Otimização de Tamanho

Do maior para menor impacto no tamanho do binário:

1. **Strip de símbolos** (fator 5–10×): `strip path/to/godot.binary` após compilar. Não funciona em binários MSVC ou Android/Web — use `debug_symbols=no` nesses casos.

2. **LTO (Link-Time Optimization)**: `scons target=template_release lto=full`. Requer ≥12 GB de RAM para linkar. Binário mais rápido E menor.

3. **optimize=size / size_extra**: `scons target=template_release optimize=size` (padrão na Web).

4. **Build profile** — detecta features usadas no projeto e desativa as não usadas:
   ```sh
   scons target=template_release build_profile=/path/to/profile.gdbuild
   ```

5. **Desabilitar Advanced Text Server** (suporte BiDi/OpenType): `module_text_server_adv_enabled=no module_text_server_fb_enabled=yes`

6. **Desabilitar 3D**: `disable_3d=yes` (~15% menor; incompatível com builds editor)

7. **Desabilitar Advanced GUI**: `disable_advanced_gui=yes` (remove Tree, RichTextLabel, CodeEdit, etc.)

8. **Desabilitar física específica**:
   - `module_jolt_enabled=no` — remove Jolt se usar GodotPhysics3D
   - `module_godot_physics_3d_enabled=no` — remove GodotPhysics3D se usar Jolt
   - `disable_physics_2d=yes` / `disable_physics_3d=yes`

9. **Desabilitar módulos não usados** (ex. para jogo 2D simples): `module_enet_enabled=no module_openxr_enabled=no module_theora_enabled=no ...` (ver lista completa em `scons --help`).

> **Regra**: use o gerador online de opções (godot-build-options-generator.github.io) para gerar um `custom.py` personalizado.

### 48.4 Compatibilidade de API (compat.inc)

Quando uma API pública é alterada (novo parâmetro, mudança de tipo de retorno), deve-se registrar um método de compatibilidade para não quebrar GDExtensions e scripts existentes:

1. Declare o método compat no `.h` (dentro de `#ifndef DISABLE_DEPRECATED`):
   ```cpp
   TypedArray<Vector2i> _get_id_path_bind_compat_88047(const Vector2i &p_from, const Vector2i &p_to);
   static void _bind_compatibility_methods();
   ```

2. Implemente em `<arquivo>.compat.inc` (ao lado do `.cpp`):
   ```cpp
   #ifndef DISABLE_DEPRECATED
   TypedArray<Vector2i> MyClass::_get_id_path_bind_compat_88047(...) {
       return get_id_path(p_from, p_to, false); // chama método novo com default antigo
   }
   void MyClass::_bind_compatibility_methods() {
       ClassDB::bind_compatibility_method(D_METHOD("get_id_path", "from_id", "to_id"),
           &MyClass::_get_id_path_bind_compat_88047);
   }
   #endif
   ```

3. Inclua o `.compat.inc` no `.cpp`: `#include "myclass.compat.inc"`

4. Valide a API com `--dump-extension-api` (master) e `--validate-extension-api` (branch):
   ```sh
   godot --dump-extension-api           # no master
   godot --validate-extension-api /path/to/extension_api.json  # no branch
   ```

5. Registre as linhas de erro em `misc/extension_api_validation/<versao-estavel>/GH-<PR>.txt` com comentário explicativo.

> **Regra**: um erro `Hash changed` indica que o binding de compatibilidade está ausente ou incorreto — os argumentos do método compat devem ser idênticos à versão anterior da API.

---

## 49. Debugging e Profiling do Engine

### 49.1 Sanitizers

Sanitizers requerem **recompilação** com flags específicos e adicionam o sufixo `.san` ao binário. São mutuamente exclusivos: ASAN, MSAN e TSAN não podem coexistir no mesmo binário.

| Sanitizer | Flag SCons | Plataformas | Overhead | Detecta |
|---|---|---|---|---|
| **ASAN** (Address) | `use_asan=yes` | Linux, macOS, Windows(MSVC), Web | ~2× | Buffer overruns, use-after-free, out-of-bounds |
| **LSAN** (Leak) | `use_lsan=yes` | Linux, Web | pequeno | Memory leaks |
| **MSAN** (Memory) | `use_msan=yes` | Linux (Clang only) | ~3× | Leitura de memória não inicializada |
| **TSAN** (Thread) | `use_tsan=yes` | Linux, macOS | ~10×, 8× mais RAM | Race conditions / data races |
| **UBSAN** | `use_ubsan=yes` | Linux, macOS, Web | pequeno | Undefined behavior em C/C++ |

**Web extras**: `use_assertions=yes` (Emscripten assertions) e `use_safe_heap=yes` (similar ao ASAN para WebAssembly).

**Detectar use-after-return com ASAN** (sem recompilar):
```sh
ASAN_OPTIONS=detect_stack_use_after_return=1 ./godot.san ...
```

> **Regra**: compile sempre com `debug_symbols=yes` para obter stack traces com referências a arquivos e linhas. Não use `strip` após compilar com sanitizers.

### 49.2 C++ Profilers

**Sampling profilers** — interrompem o programa periodicamente e estimam onde o tempo é gasto:

| Ferramenta | OS | Notas |
|---|---|---|
| VerySleepy | Windows only | Standalone, fácil de usar |
| Hotspot | Linux only | Standalone, leve |
| Instruments | macOS/iOS | Integrado na Apple |

**Tracing profilers** — registram eventos explícitos e produzem timeline:

| Ferramenta | Notas |
|---|---|
| Tracy | Cross-platform, muito popular para jogos |
| Perfetto | Cross-platform, baseado em Chrome tracing |
| Instruments | Apple only |

**Setup para profiling**:
- Compile com `production=yes debug_symbols=yes` (otimizado + símbolos).
- **Não use `strip`** após compilar — remove os símbolos necessários.
- Para medir startup/shutdown: passe `--quit` ao binário Godot.

> **Regra**: se o GDScript profiler embutido no editor não tiver resolução suficiente, use um C++ profiler externo com um build `production=yes debug_symbols=yes`.

---

## 50. Desenvolvimento do Editor e Formatos de Arquivo

### 50.1 Estrutura do Código do Editor

O editor do Godot é **escrito inteiramente em C++** — nenhum GDScript ou C# é permitido no código do editor. Ele se renderiza usando o próprio renderer e sistema de UI do Godot (não usa GTK/Qt).

**Diretório principal**: `editor/` no repositório Godot.

Arquivos chave:

| Arquivo | Papel |
|---|---|
| `editor/editor_node.cpp` | Inicialização principal do editor ("main scene" do editor) |
| `editor/project_manager/project_manager.cpp` | Project Manager |
| `editor/scene/canvas_item_editor_plugin.cpp` | Viewport 2D e ferramentas |
| `editor/scene/3d/node_3d_editor_plugin.cpp` | Viewport 3D e ferramentas |
| `editor/scene/3d/node_3d_editor_gizmos.cpp` | Gizmos 3D |

**Regra de dependência** (nunca violar):
```
editor/ → scene/ → servers/ → core/
```
Arquivos em `scene/` não podem incluir headers de `editor/`, mesmo com `#ifdef TOOLS_ENABLED`.

**Módulos do editor**: algumas features do editor vivem em `modules/` e são ativadas apenas em builds editor para reduzir tamanho dos export templates.

**Workflow de desenvolvimento**: abra o projeto de teste direto pela linha de comando para evitar passar pelo Project Manager a cada iteração:
```sh
./bin/godot.linuxbsd.editor.x86_64 --path /path/to/test_project
```

### 50.2 Ícones do Editor (SVG)

Cada classe exposta ao scripting pode ter um ícone personalizado em `editor/icons/<ClassName>.svg`.

**Requisitos**:
- Formato SVG, tamanho **16×16** px.
- Linhas snapped a pixels sempre que possível.
- Use apenas cores do mapeamento padrão (`editor/themes/editor_color_map.cpp`) para compatibilidade com temas claro/escuro — o Godot converte automaticamente as cores predefinidas para garantir contraste.

**Para ícones em projetos** (não no engine):
1. Selecione o SVG no FileSystem dock.
2. Habilite **Editor > Scale with Editor Scale** (hiDPI) no Import dock.
3. Habilite **Editor > Convert Colors with Editor Theme** (tema claro) no Import dock.
4. Clique **Reimport**.

**Otimização**: o pre-commit hook roda `svgo` automaticamente para reduzir tamanho. Mantenha o SVG fonte separado se precisar editar depois.

**Para módulos customizados**: veja `Creating custom module icons` — ícones podem ser self-contained no módulo.

### 50.3 Formato TSCN (Cenas e Resources em Texto)

O formato `.tscn` (text scene) é legível e compatível com VCS. Cenas `.escn` têm estrutura idêntica mas indicam origem externa (são compiladas para `.scn` binário na importação).

**Estrutura de um arquivo TSCN** (5 seções em ordem):

```
[gd_scene format=3 uid="uid://cecaux1sm7mo0"]  ← file descriptor

[ext_resource type="Texture2D" uid="uid://..." path="res://img.png" id="1_abc"]  ← recursos externos

[sub_resource type="SphereShape3D" id="SphereShape3D_xyz"]  ← recursos internos
radius = 1.0

[node name="Root" type="Node3D" unique_id=1234]  ← nodes
[node name="Child" type="MeshInstance3D" parent="." unique_id=5678]
mesh = SubResource("SphereShape3D_xyz")

[connection signal="pressed" from="Button" to="." method="_on_pressed"]  ← conexões de signals
```

**Regras de referência:**
- Recursos externos: `ExtResource("id_string")`
- Recursos internos: `SubResource("id_string")`
- O UID (`uid://...`) permite rastrear arquivos movidos mesmo com o editor fechado; scripts podem carregar com `uid://` como prefixo de caminho.
- Propriedades iguais ao valor padrão são omitidas (não salvas).
- Comentários com `;` são descartados ao salvar pelo editor.

**Hierarquia de nodes**: o primeiro node não tem `parent=`; filhos diretos da raiz usam `parent="."`.

```
[node name="Player" type="Node3D" unique_id=1000]                 ; raiz
[node name="Arm" type="Node3D" parent="." unique_id=1001]         ; filho da raiz
[node name="Hand" type="Node3D" parent="Arm" unique_id=1002]      ; filho de Arm
```

**NodePath**: referencia outro node ou propriedade dele. Aceita sufixo `:property` e componentes (`:scale.x`). Usado em tracks de animação e em propriedades do tipo `NodePath`.

**Animações** — estrutura de tracks em `Animation`:

| Campo | Descrição |
|---|---|
| `tracks/N/type` | `value`, `position_3d`, `rotation_3d`, `scale_3d`, `blend_shape`, `method`, `bezier`, `audio`, `animation` |
| `tracks/N/path` | `NodePath("Node:property")` — node + propriedade a animar |
| `tracks/N/interp` | 0=nearest, 1=linear, 2=cubic, 3=linear_angle, 4=cubic_angle |
| `tracks/N/keys` | Para `value`: dict com `times`, `transitions`, `update`, `values`. Para `position_3d`/`rotation_3d`/`scale_3d`: `PackedFloat32Array(T, E, X, Y, Z, ...)` |

**AnimationLibrary**: desde Godot 4, animações são agrupadas em `AnimationLibrary`. Se a library tem nome vazio, anima com `<anim_name>` diretamente; se tem nome, usa `<lib>/<anim>`.

**ArrayMesh** — superfícies em `_surfaces` (array de dicts), com campos: `vertex_data`, `vertex_count`, `index_data`, `index_count`, `attribute_data`, `format`, `primitive`, `material`, `lods`, `aabb`, `bone_aabbs`, `skin_data`, `name`.

> **Regra**: ao debugar cenas corrompidas ou geradas por código, abra o `.tscn` diretamente em um editor de texto — a estrutura legível facilita identificar recursos faltando ou hierarquia incorreta.

---

## 51. Asset Library

A Godot Asset Library (AssetLib) é um repositório de addons, scripts, ferramentas, templates e demos enviados pela comunidade, todos gratuitos e distribuídos sob licenças open source (MIT, GPL, etc.). Disponível em `godotengine.org/asset-library` e diretamente dentro do editor.

### 51.1 Tipos de Assets

Dois contextos de exibição, mutuamente exclusivos:

| Categoria | Onde aparece |
|---|---|
| **Templates**, **Projects**, **Demos** | Aba "Asset Library Projects" no **Project Manager** — são projetos standalone que funcionam sozinhos |
| Todos os outros (**Addons**, Scripts, Tools, Materials, etc.) | Aba **AssetLib** dentro de um projeto aberto no editor |

### 51.2 Usando a Asset Library no Editor

1. Abra um projeto → clique na aba **AssetLib** (ao lado de 2D, 3D, Script).
2. Pesquise por nome, categoria, licença ou versão do engine. Resultados atualizam em tempo real.
3. Clique em um asset → botão **Install** → progresso no rodapé do editor → **Package Installer**.
4. No Package Installer, desmarque arquivos indesejados e confirme com **Install**.
5. Para instalar um ZIP obtido externamente, use o botão **Import** (mesmo fluxo de instalação).

> ⚠ Evite: instalar assets de categoria "Testing" em projetos sérios — são works-in-progress.

### 51.3 Requisitos de Submissão

Um asset é **rejeitado** se violar qualquer um destes requisitos:

- **Funcionar**: o asset deve executar na versão do Godot indicada.
- **`.gitignore` correto**: remover dados redundantes do repositório.
- **Sem submodules obrigatórios**: o GitHub não inclui submodules no ZIP gerado — assets que dependem deles não funcionam.
- **Arquivo de licença**: `LICENSE` ou `LICENSE.md` com o texto completo da licença e declaração de copyright (ano(s) e titular).
- **Inglês no nome e descrição**: capitalização correta, frases completas. Outros idiomas podem ser adicionados além do inglês.
- **Icon URL direta**: para ícones hospedados no GitHub, a URL deve começar com `raw.githubusercontent.com`, não `github.com`.

### 51.4 Recomendações de Submissão

- **Pasta do addon**: coloque os arquivos em `addons/nome_do_asset/` para evitar conflitos com outros assets ou com os arquivos do usuário.
- **Sem warnings**: corrija ou suprima todos os warnings de script antes de submeter.
- **Style guide**: siga o guia oficial de estilo GDScript (ou C#).
- **Screenshots**: coloque em subpasta própria e adicione um arquivo `.gdignore` vazio nela para evitar que o Godot importe as imagens.
- **`.gitattributes`**: configure line endings (`* text=auto eol=lf`) e `export-ignore` para excluir arquivos desnecessários do ZIP da AssetLib:

```
# Addons/Asset Packs
* text=auto eol=lf
/** export-ignore
/addons !export-ignore
/addons/** !export-ignore
```

- **Cópia da licença no addon**: inclua cópia do LICENSE e README dentro da pasta do plugin — é a pasta que o usuário mantém no projeto.
- **Hospede no GitHub**: outros serviços podem ser menos confiáveis; GitHub é o mais familiar para contribuidores.

### 51.5 Formulário de Submissão — Campos

| Campo | Notas |
|---|---|
| **Asset Name** | Nome único e descritivo |
| **Category** | Addons (aparecem no editor) ou Projects/Templates/Demos (aparecem no Project Manager) |
| **Godot version** | Uma entrada por versão major; não é possível combinar múltiplas versões em um único asset |
| **Version** | Use SemVer. Há também uma versão interna incrementada a cada mudança de URL de download |
| **Repository host** | GitHub, GitLab ou Bitbucket |
| **Repository URL** | `https://github.com/<user>/<project>` |
| **Issues URL** | `https://github.com/<user>/<project>/issues` (opcional se usa o issue tracker do repo) |
| **Download Commit** | Hash completo do commit (ex.: `b1d3172f89b86e52465a74f63a74ac84c491d3e1`) |
| **Icon URL** | PNG ou JPG, proporção 1:1, mínimo 128×128 px; GitHub: `raw.githubusercontent.com/...` |
| **License** | Deve corresponder exatamente à licença no repositório |
| **Description** | Texto puro; até 3 previews (imagem ou YouTube) podem ser adicionados |

**Regra**: após enviar, o asset entra na fila de revisão manual — pode levar dias. Se rejeitado, o motivo é informado e é possível reenviar com as correções.
