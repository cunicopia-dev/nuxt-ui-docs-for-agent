<!-- source: https://ui.nuxt.com/components/dashboard-search --> # DashboardSearchPRO

[CommandPalette](/components/command-
palette)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardSearch.vue)

A ready to use CommandPalette to add to your dashboard.

## Usage

The DashboardSearch component extends the
[CommandPalette](/components/command-palette) component, so you can pass any
property such as `icon`, `placeholder`, etc.

Use it inside the default slot of the [DashboardGroup](/components/dashboard-
group) component:

layouts/dashboard.vue

    
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar>
          <UDashboardSearchButton />
        </UDashboardSidebar>
    
        <UDashboardSearch />
    
        <slot />
      </UDashboardGroup>
    </template>
    

You can open the CommandPalette by pressing ` ``K`, by using the
[DashboardSearchButton](/components/dashboard-search-button) component or by
using a `v-model:open` directive.

### Shortcut

Use the `shortcut` prop to change the shortcut used in
[defineShortcuts](/composables/define-shortcuts) to open the ContentSearch
component. Defaults to `meta_k` (` ` `K`).

app.vue

    
    
    <template>
      <UDashboardSearch
        v-model:search-term="searchTerm"
        shortcut="meta_k"
        :groups="groups"
        :fuse="{ resultLimit: 42 }"
      />
    </template>
    

### Color Mode

By default, a group of commands will be added to the command palette so you
can switch between light and dark mode. This will only take effect if the
`colorMode` is not forced in a specific page which can be achieved through
`definePageMeta`:

pages/index.vue

    
    
    <script setup lang="ts">
    definePageMeta({
      colorMode: 'dark'
    })
    </script>
    

You can disable this behavior by setting the `color-mode` prop to `false`:

app.vue

    
    
    <template>
      <UDashboardSearch
        v-model:search-term="searchTerm"
        :color-mode="false"
        :groups="groups"
        :fuse="{ resultLimit: 42 }"
      />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`colorMode`| `true`| `boolean`  
`shortcut`| `'meta_k'`| ` string`  
`icon`| `appConfig.ui.icons.search`| ` string`The icon displayed in the search
input.  
`open`| | `boolean`  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`searchTerm`| | ` string`  
`placeholder`| | ` string`Placeholder for the command palette search input.  
`groups`| | ` CommandPaletteGroup<CommandPaletteItem>[]`  
`fuse`| `{}`| ` UseFuseOptions<CommandPaletteItem>`Options for
[useFuse](https://vueuse.org/integrations/useFuse) passed to the
[CommandPalette](https://ui.nuxt.com/components/command-palette).  
`ui`| | ` { modal?: ClassNameValue; input?: ClassNameValue; } & { root?: ClassNameValue; input?: ClassNameValue; close?: ClassNameValue; ... 19 more ...; itemLabelSuffix?: ClassNameValue; }`Show properties

  * `modal?: ClassNameValue`
  * `input?: ClassNameValue`
  * `root?: ClassNameValue`
  * `close?: ClassNameValue`
  * `content?: ClassNameValue`
  * `viewport?: ClassNameValue`
  * `group?: ClassNameValue`
  * `empty?: ClassNameValue`
  * `label?: ClassNameValue`
  * `item?: ClassNameValue`
  * `itemLeadingIcon?: ClassNameValue`
  * `itemLeadingAvatar?: ClassNameValue`
  * `itemLeadingAvatarSize?: ClassNameValue`
  * `itemLeadingChip?: ClassNameValue`
  * `itemLeadingChipSize?: ClassNameValue`
  * `itemTrailing?: ClassNameValue`
  * `itemTrailingIcon?: ClassNameValue`
  * `itemTrailingHighlightedIcon?: ClassNameValue`
  * `itemTrailingKbds?: ClassNameValue`
  * `itemTrailingKbdsSize?: ClassNameValue`
  * `itemLabel?: ClassNameValue`
  * `itemLabelBase?: ClassNameValue`
  * `itemLabelPrefix?: ClassNameValue`
  * `itemLabelSuffix?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`empty`| `{ searchTerm?: string | undefined; }`  
`close`| `{ ui: { root: (props?: Record<string, any> | undefined) => string; input: (props?: Record<string, any> | undefined) => string; close: (props?: Record<string, any> | undefined) => string; ... 19 more ...; itemLabelSuffix: (props?: Record<...> | undefined) => string; }; }`  
`item`| `{ item: CommandPaletteItem; index: number; }`  
`item-leading`| `{ item: CommandPaletteItem; index: number; }`  
`item-label`| `{ item: CommandPaletteItem; index: number; }`  
`item-trailing`| `{ item: CommandPaletteItem; index: number; }`  
`content`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[value: boolean]`  
`update:searchTerm`| `[value: string]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardSearch: {
          slots: {
            modal: 'sm:max-w-3xl sm:h-[28rem]',
            input: '[&>input]:text-base/5'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            dashboardSearch: {
              slots: {
                modal: 'sm:max-w-3xl sm:h-[28rem]',
                input: '[&>input]:text-base/5'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            dashboardSearch: {
              slots: {
                modal: 'sm:max-w-3xl sm:h-[28rem]',
                input: '[&>input]:text-base/5'
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardResizeHandleA handle to resize a sidebar or
panel.](/components/dashboard-resize-handle)[DashboardSearchButtonA pre-styled
Button to open the DashboardSearch modal.](/components/dashboard-search-
button)

