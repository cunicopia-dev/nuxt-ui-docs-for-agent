<!-- source: https://ui.nuxt.com/components/content-search-button --> # ContentSearchButtonPRO

[Button](/components/button)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/content/ContentSearchButton.vue)

A pre-styled Button to open the ContentSearch modal.

[](/getting-started/content)This component is only available when the
`@nuxt/content` module is installed.

## Usage

The ContentSearchButton component is used to open the
[ContentSearch](/components/content-search) modal.

    
    
    <template>
      <UContentSearchButton />
    </template>
    

It extends the [Button](/components/button) component, so you can pass any
property such as `color`, `variant`, `size`, etc.

    
    
    <template>
      <UContentSearchButton variant="subtle" />
    </template>
    

The button defaults to `color="neutral"` and `variant="outline"` when not
collapsed, `variant="ghost"` when collapsed.

### Collapsed

Use the `collapsed` prop to show the button's label and kbds. Defaults to
`true`.

collapsed

false

    
    
    <template>
      <UContentSearchButton :collapsed="false" />
    </template>
    

### Kbds

Use the `kbds` prop to display keyboard keys in the button. Defaults to
`['meta', 'K']` to match the default shortcut of the
[ContentSearch](/components/content-search#shortcut) component.

collapsed

false

    
    
    <template>
      <UContentSearchButton :collapsed="false" :kbds="['alt', 'O']" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`color`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`collapsed`| `true`| `boolean`  
`kbds`| `["meta", "k"]`| ` (string | undefined)[] | KbdProps[]`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'kbd'`.
  * `value?: string`
  * `variant?: "solid" | "outline" | "subtle"`Defaults to `'outline'`.
  * `size?: "md" | "sm" | "lg"`Defaults to `'md'`.
  * `class?: any`

  
`icon`| `appConfig.ui.icons.search`| ` string`The icon displayed in the
button.  
`label`| `t('contentSearchButton.label')`| ` string`The label displayed in the
button.  
`size`| | ` "md" | "xs" | "sm" | "lg" | "xl"`  
`variant`| | ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`The variant of the button. Defaults to 'outline' when not collapsed, 'ghost' when collapsed.  
`ui`| | ` { base?: ClassNameValue; trailing?: ClassNameValue; } & { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`Show properties

  * `base?: ClassNameValue`
  * `trailing?: ClassNameValue`
  * `label?: ClassNameValue`
  * `leadingIcon?: ClassNameValue`
  * `leadingAvatar?: ClassNameValue`
  * `leadingAvatarSize?: ClassNameValue`
  * `trailingIcon?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        contentSearchButton: {
          slots: {
            base: '',
            trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
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
            contentSearchButton: {
              slots: {
                base: '',
                trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
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
            contentSearchButton: {
              slots: {
                base: '',
                trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ContentSearchA ready to use CommandPalette to add to your
documentation.](/components/content-search)[ContentSurroundA pair of prev and
next links to navigate between pages.](/components/content-surround)

